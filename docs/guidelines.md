# Guidelines

## Getting the repository

To get the repository on your local machine open a terminal in  folder of your computer. Your ``home`` folder is usually a good choice. Then run the following commands:

```bash
git clone https://github.com/NicholasCorniaOrpheus/decastrophizing-failure-through-playfulness.git
```
A copy of the [GitHub repository](https://github.com/NicholasCorniaOrpheus/decastrophizing-failure-through-playfulness) will now be available.

```bash
# Get in the GitHub directory
cd ./decastrophizing-failure-through-playfulness
#Set the default branch to gh-pages
git checkout --orphan gh-pages
```

Test if you can commit changes:

```bash
# Add local changes
git add .
# Commit message
git commit --allow-empty -m "Test"
# Push the changes back to the repository
git push origin gh-pages
```

## Routine script

Make sure you are working with an updated version of the repository. You can pull the latest version by running the command:

```bash
git pull
```

Item pages, in Markdown format, will be available at the ``docs`` folder.

You can modify the context of an item using _Sublime Text_, or create a new one copying the ``prototype.md`` page in a new file.

To push the changes back to the repository run the following commands in terminal:

```bash
git add .
# commit with current date message
git commit -m date '+%Y-%m-%d'
# push to gh-pages branch
git push origin gh-pages
```

## Markdown cheatsheet

| name          | syntax                         | result                      |
| ------------- | ------------------------------ | --------------------------- |
| italic        | ``_text_``                     | _text_                      |
| bold          | ``**text**``                   | **text**                    |
| hyperlink     | ``[text](url)``                | [text](url)                 |
| citation      | ``text[^1].  [^1]: citation.`` | text [^1].  [^1]: citation. |
| internal link | ``[text](./page_name.md)``     | [text](./page.md)           |
| ...           |                                |                             |
