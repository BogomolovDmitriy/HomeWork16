
def creat(data):
    html = '<html>\n <head></head>\n <body>\n'
    style = 'style="font-size:22px;"'
    for i in data:
        html += '    <p {}> user: {} </p>\n'\
            .format(style, i)
    html += '   </body>\n</html>'

    with open('index.html', "w") as page:
        page.write(html)
    
    return data
