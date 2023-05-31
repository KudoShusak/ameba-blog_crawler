# ameba blog crawler
アメーバブログ `www.ameba.jp` から記事を収集します。  
Collect articles from the Ameba blog `www.ameba.jp`.

## execution 
```
% python crawling_ameba-blog.py
```

カレントディレクトリに３種類のファイル、`xxxxxxxx_xxxxxx_ameba-blog.jsonl`と、`xxxxxxxx_xxxxxx_ameba-blog_cwlLog.jsonl`、`xxxxxxxx_xxxxxx_ameba-blog_html_list.jsonl`が出力されます。  
また、`xxxxxxxx_xxxxxx_html`という名前のフォルダに、収集したhtmlファイルが保存されます。  
（`xxxxxxxx_xxxxxx`には、実行した日付と時刻からユニークな文字列が入ります）  
Three files `xxxxxxxxxxxxxx_ameba-blog.jsonl`, `xxxxxxxxxxxxxx_ameba-blog_cwlLog.jsonl` and `xxxxxxxxxxxxxx_ameba-blog_html _list.jsonl` will be output in the current directory.  
In addition, the collected html files will be saved in a folder named `xxxxxxxxxxxx_xxxxxx_html`.  
(where `xxxxxxxxxxxx_xxxxxxxx` is a unique string from the date and time of execution)

* `xxxxxxxxxxxxxx_ameba-blog.jsonl`  
記事のURLと記事のテキストデータが保存されます。  
The text data of the article is saved.
* `xxxxxxxxxxxxxx_ameba-blog_cwlLog.jsonl`  
クロールしたURLと、htmlから抽出した記事のデータ（htmlタグ付きと、テキストデータ）が保存されます。  
The crawled URL and the article data (html tagged and text data) extracted from the html are saved.
* `xxxxxxxxxxxxxx_ameba-blog_html _list.jsonl`  
`xxxxxxxxxxxx_xxxxxx_html`に保存されているhtmlのファイル名と、収集元のURLが保存されます。  
The file name of the html file stored in `xxxxxxxxxxxxxxxxx_xxxxxxxxx_html` and the URL of the collection source will be saved.
* `xxxxxxxxxxxx_xxxxxx_html`  
収集したhtmlはこのフォルダに保存されます。  
The collected html is stored in this folder.

## Saved data format

### xxxxxxxxxxxxxx_ameba-blog.jsonl

１記事につき、１行のJSONフォーマットで保存されます。（JSONLフォーマット）内容は下記の通り。  
One line per article will be saved in JSON format.(JSONL Format) The contents are as follows

```
{"url": "https://www....", "text":"Article Data"}
{"url": "https://www....", "text":"Article Data"}
{"url": "https://www....", "text":"Article Data"}
.....
```

Example.
```
{"url": "https://ameblo.jp/kumikotakeda/entry-12805291014.html", "text": "本日の巻き髪\n \n \n \n \n今日は朝からQVCの生出演！\n \n朝5時起きで頑張っています。\n \n午前中の髪型をヘア担当の石倉さんと\n \nたまには変えてみようか？と考えましたが、\nやはり私のトレードマークでもある\n \nこの髪型にしました〜❣️\n \nでも毎回同じでは無く\n \n微妙に巻き髪スタイルの巻き方が\n \n違うんですよ！^_^\n \n \n \n本日この後も8時からと9時から\n \n私がプロデュースしたノンワイヤー\n \n美バストブラのオンセールです！\n \n是非ともご覧下さい\n \n \n \n \n "}
{"url": "https://ameblo.jp/kawata--hiromi/entry-12805341645.html", "text": "毎夜の光景\n5月31日（水）18:25〜\n今日も子供たちと遊んでくれて\nおもちゃの皆さん！\nありがとうございました"}
{"url": "https://ameblo.jp/hiranonora/entry-12805304197.html", "text": "世界のポケモン\nポケモンが土地転がしてました💛\nよくわからないけど\nキュートなゴミ箱！\nどんどんゴミ食べさせたくなっちゃうね💚\nフロアにちょっとしたキッズが遊べるプレイスペース！\nこーゆーの助かるわぁ〜\n大人もひと息\n赤ちゃんもいて萌えキュン太郎！\nバブ子は積み上げと破壊を繰り返して\nひれ伏す！\n母はユニーク靴下を履いて来た事をはじめて少し恥ずかしいと感じた🫣\nさて、スーミーが観たがっているステージがはじまる\n💚発売中\nよろしくおねがいします！"}
```

### xxxxxxxxxxxxxx_ameba-blog_cwlLog.jsonl

１記事につき、１行のJSONフォーマットで保存されます。（JSONLフォーマット）内容は下記の通り。  
One line per article will be saved in JSON format.(JSONL Format) The contents are as follows
```
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
.....
```

Example.
```
{"url": "https://ameblo.jp/kumikotakeda/entry-12805291014.html", "contents": ["[<h1 class=\"skin-entryTitle\" data-uranus-component=\"entryTitle\"><a aria-current=\"page\" class=\"skinArticleTitle\" href=\"/kumikotakeda/entry-12805291014.html\" rel=\"bookmark\">本日の巻き髪</a></h1>, <p> </p>, <p> </p>, <p> </p>, <p> </p>, <p>今日は朝からQVCの生出演！</p>, <p> </p>, <p>朝5時起きで頑張っています。</p>, <p> </p>, <p>午前中の髪型をヘア担当の石倉さんと</p>, <p> </p>, <p>たまには 変えてみようか？と考えましたが、</p>, <p>やはり私のトレードマークでもある</p>, <p> </p>, <p>この髪型にしました〜❣️</p>, <p> </p>, <p>でも毎回同じでは無く</p>, <p> </p>, <p>微妙に巻き髪スタイルの巻き方が</p>, <p> </p>, <p>違うんですよ！^_^</p>, <p> </p>, <p> </p>, <p> </p>, <p>本日この後も8時からと9時から</p>, <p> </p>, <p>私がプロデュースしたノンワイヤー</p>, <p> </p>, <p>美バストブラのオンセールです！</p>, <p> </p>, <p>是非ともご覧下さい<img alt=\"ビックリマーク\" class=\"emoji\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char2/039.gif\"/><noscript><img alt=\"ビックリマーク\" class=\"emoji\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char2/039.gif\"/></noscript><img alt=\"ビックリマーク\" class=\"emoji\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char2/039.gif\"/><noscript><img alt=\"ビックリマーク\" class=\"emoji\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char2/039.gif\"/></noscript><img alt=\"ビックリマーク\" class=\"emoji\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char2/039.gif\"/><noscript><img alt=\"ビックリマーク\" class=\"emoji\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char2/039.gif\"/></noscript></p>, <p> </p>, <p> </p>, <p> </p>, <p> </p>, <p> </p>]", ["本日の巻き髪", " ", " ", " ", " ", "今日は朝からQVCの生出演！", " ", "朝5時起きで頑張っています。", " ", "午前中の髪型をヘア担当の石倉さんと", " ", "たまには変えてみようか？と考えましたが、", "やはり私のトレードマークでもある", " ", "この髪型にしました〜❣️", " ", "でも毎回同じでは無く", " ", "微妙に巻き髪スタイルの巻き方が", " ", "違うんですよ！^_^", " ", " ", " ", "本日この後も8時からと9時から", " ", "私がプロデュースしたノンワイヤー", " ", "美バストブラのオンセールです！", " ", "是非ともご覧下さい", " ", " ", " ", " ", " "]]}
{"url": "https://ameblo.jp/kawata--hiromi/entry-12805341645.html", "contents": ["[<h1 class=\"skin-entryTitle\" data-uranus-component=\"entryTitle\"><a aria-current=\"page\" class=\"skinArticleTitle\" href=\"/kawata--hiromi/entry-12805341645.html\" rel=\"bookmark\">毎夜の光景</a></h1>, <div><span style='font-size: 16px; caret-color: rgb(43, 46, 56); color: rgb(43, 46, 56); font-family: lato, \"ヒラギノ角ゴ ProN W3\", \"Hiragino Kaku Gothic ProN\", メイリオ, \"Helvetica Neue\", Helvetica, Arial, sans-serif; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); -webkit-text-size-adjust: 100%; background-color: rgb(255, 255, 255);'>5月31日（水）18:25〜</span></div>, <div><font color=\"#2b2e38\" face=\"lato, ヒラギノ角ゴ ProN W3, Hiragino Kaku Gothic ProN, メイリオ, Helvetica Neue, Helvetica, Arial, sans-serif\"><span style=\"caret-color: rgb(43, 46, 56); -webkit-tap-highlight-color: rgba(0, 0, 0, 0); -webkit-text-size-adjust: 100%; background-color: rgb(255, 255, 255);\">今日も子供たちと遊んでくれて</span></font></div>, <div><font color=\"#2b2e38\" face=\"lato, ヒラギノ角ゴ ProN W3, Hiragino Kaku Gothic ProN, メイリオ, Helvetica Neue, Helvetica, Arial, sans-serif\"><span style=\"caret-color: rgb(43, 46, 56); -webkit-tap-highlight-color: rgba(0, 0, 0, 0); -webkit-text-size-adjust: 100%; background-color: rgb(255, 255, 255);\">おもちゃの皆さん！</span></font></div>, <div><font color=\"#2b2e38\" face=\"lato, ヒラギノ角ゴ ProN W3, Hiragino Kaku Gothic ProN, メイリオ, Helvetica Neue, Helvetica, Arial, sans-serif\"><span style=\"-webkit-tap-highlight-color: rgba(0, 0, 0, 0); -webkit-text-size-adjust: 100%; background-color: rgb(255, 255, 255);\">ありがとうございました</span></font><img alt=\"うさぎのぬいぐるみ\" class=\"emoji\" height=\"24\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char4/667.png\" style=\"aspect-ratio: 24 / 24;\" width=\"24\"/><noscript><img alt=\"うさぎのぬいぐるみ\" class=\"emoji\" height=\"24\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char4/667.png\" width=\"24\"/></noscript><img alt=\"ハイハイ\" class=\"emoji\" height=\"24\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char4/649.png\" style=\"aspect-ratio: 24 / 24;\" width=\"24\"/><noscript><img alt=\"ハイハイ\" class=\"emoji\" height=\"24\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char4/649.png\" width=\"24\"/></noscript></div>]", ["毎夜の光景", "5月31日（水）18:25〜", "今日も子供たちと遊んでくれて", "おもちゃの皆さん！", "ありがとうございました"]]}
{"url": "https://ameblo.jp/hiranonora/entry-12805304197.html", "contents": ["[<h1 class=\"skin-entryTitle\" data-uranus-component=\"entryTitle\"><a aria-current=\"page\" class=\"skinArticleTitle\" href=\"/hiranonora/entry-12805304197.html\" rel=\"bookmark\">世界のポケモン</a></h1>, <div><font size=\"5\">ポケモンが土地転がしてました💛</font></div>, <p><font size=\"5\">よくわからないけど</font></p>, <p><font size=\"5\">キュートなゴミ箱！</font></p>, <p><font size=\"5\">どんどんゴミ食べさせたくなっちゃうね💚</font></p>, <p><font size=\"5\">フロアにちょっとしたキッズが遊べるプレイスペース！</font></p>, <p><font size=\"5\">こーゆーの助かるわぁ〜</font></p>, <p><font size=\"5\">大人もひと息</font></p>, <p><font size=\"5\">赤ちゃんもいて萌えキュン太郎！</font></p>, <p><font size=\"5\">バブ子は積み上げと破壊を繰り返して</font></p>, <p><font size=\"5\">ひれ伏す！</font></p>, <p><font size=\"5\">母はユニーク靴下を履いて来た事をはじめて少し恥ずかしいと感じ た🫣</font></p>, <p><font size=\"5\">さて、スーミーが観たがっているステージがはじまる</font><img alt=\"指差し\" class=\"emoji\" height=\"24\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char4/602.png\" style=\"aspect-ratio: 24 / 24;\" width=\"24\"/><noscript><img alt=\"指差し\" class=\"emoji\" height=\"24\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char4/602.png\" width=\"24\"/></noscript><img alt=\"飛び出すハート\" class=\"emoji\" height=\"24\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char4/610.png\" style=\"aspect-ratio: 24 / 24;\" width=\"24\"/><noscript><img alt=\"飛び 出すハート\" class=\"emoji\" height=\"24\" src=\"https://stat100.ameba.jp/blog/ucs/img/char/char4/610.png\" width=\"24\"/></noscript></p>, <p>💚発売中</p>, <p>よろしくおねがいします！</p>]", ["世界のポケモン", "ポケモンが土地転がしてました�"", "よくわからないけど", "キュートなゴミ箱！", "どんどんゴミ食べさせたくなっちゃうね💚", "フロアにちょっとしたキッズが 遊べるプレイスペース！", "こーゆーの助かるわぁ〜", "大人もひと息", "赤ちゃんもいて萌えキュン太郎！", "バブ子は積み上げと破壊を繰り返して", "ひれ伏す！", "母はユニーク靴下を履いて来た事をはじめて少し恥ずかしいと感じた🫣", "さて、スーミーが観たがっているステージがはじまる", "💚発売中", "よろしくおねがいします！"]]}
```

### xxxxxxxxxxxxxx_ameba-blog_html _list.jsonl

`xxxxxxxxxxxx_xxxxxx_html`に保存されているhtmlのファイル名と、収集元のURLがJSONL形式で保存されます。  
The html file name stored in `xxxxxxxxxxxxxxxxx_xxxxxxxxx_html` and the URL of the collection source will be saved in JSONL format.

```
{"filename": "xxxxx_ameba-blog_article.html", "url": "https://www......."}
{"filename": "xxxxx_ameba-blog_article.html", "url": "https://www......."}
{"filename": "xxxxx_ameba-blog_article.html", "url": "https://www......."}
.....
```

Example.
```
{"filename": "00001_ameba-blog_article.html", "url": "https://ameblo.jp/kumikotakeda/entry-12805291014.html"}
{"filename": "00002_ameba-blog_article.html", "url": "https://ameblo.jp/kawata--hiromi/entry-12805341645.html"}
{"filename": "00003_ameba-blog_article.html", "url": "https://ameblo.jp/hiranonora/entry-12805304197.html"}
```

### xxxxxxxxxxxx_xxxxxx_html

収集したhtmlはこのフォルダに保存されます。  
The collected html is stored in this folder.

個々のファイルの名前は５桁の数字の後に`_ameba-blog_article.html`を付けたものになります。  
The name of each individual file will be a five-digit number followed by `_ameba-blog_article.html`.