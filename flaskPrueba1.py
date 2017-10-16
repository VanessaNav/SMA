import httplib2

def getHello():
    url = ('http://localhost:5000/readHello')
    h = httplib2.Http() #crear cliente http
    (response, content) = h.request(url,'GET')
    return content

print(getHello())