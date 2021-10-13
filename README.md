
## ⚠️ 注意1：项目有bug，需要修改notion-py/notion/store.py的limit:100才能使用
> 参考：https://github.com/jamalex/notion-py/issues/292

## ⚠️ 注意2：项目运行，不用运行setup.sh，装包后运行以下即可
```zsh
streamlit run notion-md-exporter.py
```

## ⚠️ 注意3：streamlit 依赖python3.7, 记得在pycharm配置好开发环境
1. pycharm会自动提示创建新环境运行项目
2. 如果没有提示，在finder中删除.venv文件夹即可
3. 安装python3.7后再配置项目


## Introduction

This web-based app can help you to batch export notion pages to Markdown format correctly. 

Please follow these simple steps.

Step 1. [Open this link](http://notion-to-markdown.herokuapp.com/), and you will see the web interface.

![](assets/2020-07-16-22-36-52-895669.png)

Step 2. Get your notion token_v2 and input it in the first textbox. You can learn how to get your token by [reading this web page](https://www.redgregory.com/notion/2020/6/15/9zuzav95gwzwewdu1dspweqbv481s5).

Step 3. Move **all the pages** you want to export to a new page. 

![](assets/2020-07-16-22-36-53-795056.png)

As you may see, links to pages are also acceptable. In this case, you don't need to move the pages at all.

Step 4. Please copy the link to the new page and input it in the second textbox and press Enter. 

![](assets/2020-07-16-22-36-54-695166.png)

Step 5. You will see a new button named "export." Click it.

![](assets/2020-07-16-22-36-55-407341.png)

Step 6. When you see a new link named "Click to download" shown on the web page, click it and download a zip file. Extract it, and you will find all the Markdown files as well as the images.

![](assets/2020-07-16-22-36-56-394616.png)
![](assets/2020-07-16-22-36-57-445010.png)

Step 7. (Optional) You can drag the folder to Obsidian's Root Directory and browse the Markdown files.

![](assets/2020-07-16-22-36-59-197396.png)

As you can see here, all the titles of pages are kept as the name of Markdown files.

In contrast, if you export the Markdown files using the default export function in notion, you will get an extracted directory like this.

![](assets/2020-07-16-22-37-00-245922.png)

If you put it into Obsidian, you will realize the linked sub-page was not downloaded at all.

![](assets/2020-07-16-22-37-01-351948.png)

Besides, in the subfolder, there is no image file. The image is still in the cloud.

![](assets/2020-07-16-22-37-02-563403.png)

If you like this app, please add a star to [my Github Repo](https://github.com/wshuyi/demo-notion-markdown-exporter). Thanks! 

That's all. Enjoy! :)

## Acknowledgement

This Web app is developed by [Shuyi Wang](https://twitter.com/wshuyi) based on [Eunchan Cho(@echo724)\'s notion2md](https://github.com/echo724/notion2md)

