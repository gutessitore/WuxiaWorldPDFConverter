def getUrl(url):
    fullUrl = url
    stripedUrl = url.split("/")
    sufix = stripedUrl[-1]
    chapter = sufix.split("-")[-1]
    cleanSufix = sufix.replace(chapter, "")
    novel = stripedUrl[-2]
    noChapterUrl = fullUrl.replace(stripedUrl[-1], cleanSufix)
    return novel, noChapterUrl


def urlChapterGenerator(noChapterUrl, chapterStart, chapterEnd, step=1):
    chapters = [str(chapter) for chapter in range(chapterStart, chapterEnd + 1, step)]
    urls = [noChapterUrl + chapter for chapter in chapters]
    return urls
