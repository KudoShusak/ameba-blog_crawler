import re
import requests
import time
import os
from datetime import datetime
import json
from bs4 import BeautifulSoup

# クローリングを開始するURL
start_url = "https://www.ameba.jp/"

prefix = '{:%Y%m%d_%H%M%S}_'.format(datetime.now())

# クローリング結果保存ファイル
result_file = f"{prefix}ameba-blog_cwlLog.jsonl"

# テキストデータ保存ファイル
text_file = f"{prefix}ameba-blog.jsonl"

# 取得したhtmlのリストを保存するファイル
logfile = f"{prefix}ameba-blog_html_list.jsonl"

# htmlファイルの名前
sub_filename = "_ameba-blog_article.html"

# htmlファイルを保存するディレクトリ（フォルダ）
directory = f'{prefix}html'
os.mkdir(directory)

#### テキスト抽出 ####

def gettext(soup):

    txthtmllist = []
    txtlist = []

    # <html>タグのクラスによってブログのフォーマットが大きく変わることが判明
    # classを抽出
    htmlstr = str(soup).replace('\n', '')
    html_class = re.match('.+?class="(.+?)"', str(htmlstr)).group(1)

    if html_class == "fixed" : # LiLiCoさんのブログで発覚
        blogmain = soup.find('div', id='main')

        # 各行を<div>タグでくくるパターンと<p>タグでくくるパターンが存在して、
        # それぞれ、フォーマットが違う。
        LiLiCo_flg = False
        contents = blogmain.find('div', class_='contents')
        for sentence in contents.find_all('p'):
            if sentence != None :
                if sentence.text != '' :
                    LiLiCo_flg = True

        Junichi_flg = False
        for sentence in contents.find_all('div', class_=''):
            if sentence != None :
                if sentence.text != '' :
                    Junichi_flg = True

        if LiLiCo_flg == True :
            # LiLiCoさんパターン
            for sentence in blogmain.find_all(['p','h1','h2','h3','h4']):
                txthtmllist.append(sentence)
                txtlist.append(sentence.text)

        elif Junichi_flg == True :
            # 新田純一さんパターン
            title = blogmain.find(['h1','h2','h3'], class_='title')
            txthtmllist.append(title)
            txtlist.append(title.text)

            for sentence in contents.find_all('div', class_=''):
                txthtmllist.append(sentence)
                txtlist.append(sentence.text)
        
        else :
            # <p>でも<div>でも囲われていない場合もある
            title = blogmain.find(['h1','h2','h3'], class_='title')
            txthtmllist.append(title)
            txtlist.append(title.text)

            txthtmllist.append(contents)
            # <br/>タグを'\n'に置換し、テキストデータに筆者の改行の意図を残す
            text_data = str(contents).replace('<br/>', '\n')
            minisoup = BeautifulSoup(text_data, "html.parser")
            txtlist.append(minisoup.text)

    else : # ほとんどはこちらで対応可能
        # 広告の文字列が混入するのを防ぐためにできるだけタグを絞り込みたい
        element = soup.find('div', class_='skin-entryInner')
        if element == None:
            element = soup.find('div', class_='skinArticle3') # エビちゃんのブログで発覚

        # タイトル行の取得
        title = element.find(class_='skin-entryTitle')
        if title == None :
            title = element.find('h1') # エビちゃんのブログで発覚

        txthtmllist.append(title)
        txtlist.append(title.text)

        # 記事本文の取得
        article = element.find('div', id='entryBody')

        # 各文章を<p>タグで囲っているブログと<div>タグで囲っているブログがある。
        # 本文の中に<h1>等のタイトルタグを使っているブログがある。（サンド富澤さんのブログで発覚）
        for sentence in article.find_all(['p','div','h1','h2','h3']):
            # 広告テキストの混入回避(1)
            if sentence.find('article') == None and sentence.text != '':
                # <div>タグの中に<p>タグがある場合、二重に取得してしまうことを回避
                if sentence.find('p') == None:
                    # <br/>タグで改行している場合の対処（一旦strにキャストして<br/>を'\n'に置換）
                    nobrtxt = str(sentence).replace('<br/>','\n')
                    # 広告テキストの混入回避(2)
                    ## クラス名取得
                    classtext = re.match('<[^>]+?class="(.+?)"',nobrtxt)
                    if classtext == None :
                        classname = ""
                    else :
                        classname = classtext.group(1)
                    ## クラス名を参照し、広告以外を選んでテキスト抽出
                    if classname in ["", "title", "p1", "p2", "p3", "p4"] : # p1~4は河村隆一さんのブログで発覚
                        # 再度パースしてテキストのみ抽出
                        minisoup = BeautifulSoup(nobrtxt, "html.parser")
                        txthtmllist.append(minisoup)
                        txtlist.append(minisoup.text)

    return [txthtmllist,txtlist]

#### JSONL形式で保存 ####

# save_dataをJSON形式でresult_fileに追記する。
def save_result(cont_txt, url="None", filename=result_file):

    save_data = {"url":url, "contents": [str(cont_txt[0]), cont_txt[1]]}

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(save_data, ensure_ascii=False) + '\n')
    f.close()

    return

# テキストデータのlistを指定の形式でtext_fileに追記する
def save_text(textlist, url="None", filename=text_file):

    jointxt = '\n'.join(textlist)
    save_data = {"url" : url, "text" : jointxt}

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(save_data, ensure_ascii=False) + '\n')
    f.close()

    return

#### クローリング ####

# アクセスするURL(初期値はクローリングを開始するURL)
url = start_url
urllist = [url]

# クロール済みリスト
crawledlist = []

count = 0
for i in range(4):
    print(f'{i + 1}階層目クローリング開始')

    linklist = []
    # 対象ページのhtml取得
    for url in urllist:
        #　同じURLを何度もクロールしない
        if url in crawledlist:
            continue

        time.sleep(3) # データ取得前に少し待つ

        try:
            html = requests.get(url)
            soup = BeautifulSoup(html.content, "html.parser")
            # 次のループで使うURLの候補として<a>タグのリストをため込む

            linklist.extend(soup.find_all("a"))

            ## テキスト抽出
            if '/entry-' in url :
                count += 1

                cont_txt = gettext(soup)
                save_result(cont_txt, url=url, filename = result_file)
                save_text(cont_txt[1], url=url, filename = text_file)
                print(count, cont_txt[1])

                # 取得したhtmlをファイルに保存
                filename = str(count).zfill(5) + sub_filename
                filepath = os.path.join(directory,filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(str(html.text))
                f.close()

                # ファイル名とurlのセットを記録しておく
                logdata = {'filename': filename, 'url': url}
                with open(logfile, 'a', encoding='utf-8') as f:
                    f.write(json.dumps(logdata)+'\n')
                f.close()

        except:
            # 何かエラーが出てもとりあえず続ける
            print(f'Error: {url}')
            continue

    # 使い終わったurllistをクロール済みリストに追加
    crawledlist.extend(urllist)
    crawledlist = list(set(crawledlist)) # 重複削除

    # 次のループのためのurllistを作る
    urllist = []
    for link in linklist:
        # 取得した<a>タグのリストから、ブログ記事であることを期待して"/entry-"が含まれているURLを取得
        for url in re.findall('<a.+?href="(.+?/entry-.+?)".*?>', str(link)):
            # 同じ記事を何度もクロールしないように'?'と'#'の後の文字列を削除
            url = re.sub('[?#].+','',url)
            # urlが'/'で始まっていたら先頭に'https://ameblo.jp'を補完
            if url[0] == '/' :
                url = f'https://ameblo.jp{url}'
            urllist.append(url)
    
    # 新着ブログが載るページを追加
    fixedlist = ['https://www.ameba.jp/','https://official.ameba.jp/rankings/hot','https://blogger.ameba.jp/ranking/daily']
    urllist.extend(fixedlist)
    urllist = list(set(urllist)) # 重複削除

    # クロール済みリストから、新着ブログが載るページを削除
    for fixed in fixedlist:
        crawledlist= [s for s in crawledlist if s != fixed]
