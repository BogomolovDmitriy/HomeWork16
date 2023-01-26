
def creat(data):
    t = data
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}> Temperature: {} c</p>\n'\
        .format(style, t)
    html += '   </body>\n</html>'

    with open('index.html', "w") as page:
        page.write(html)
    
    return data
