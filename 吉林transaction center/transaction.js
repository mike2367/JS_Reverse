stringChangeASCIINumberArrs = function(e) {
    for (var t = [], n = 0; n < e.length; n++)
        t.push(e.charCodeAt(n));
    return t
}
random = function(e, t) {
    return void 0 === e && (e = 0),
    void 0 === t && (t = 1e4),
    Math.floor(Math.random() * (t - e) + e)
}
randomStr = function(e) {
    for (var t = [], n = 0; n < e; n++)
        t.push(random(0, 35).toString(36));
    return t.join("")
}
encrypt = function(page) {
    e = "{\"id\":\"rtnn4ncshjk4l2lc\",\"projectKey\":\"honsan_cloud_ccprec\",\"clientKey\":\"rtnn4ncqdxcf7qkr\",\"token\":null,\"clientDailyData\":{},\"acts\":[{\"id\":\"rtnn4ncqzj4unc33\",\"fullPath\":\"/ccprec.com.cn.web/client/info/cqweb_nonphy_cqzr\",\"args\":["+ page +",20,null]}]}"
    pubPass = "BX1o65CoobwcDP33iQW6ld1OyIPsNzF1",
    pubPassNum = stringChangeASCIINumberArrs(pubPass);
    e = JSON.stringify(e);
    for (var t = encodeURI(e), n = [], i = 0, r = "", o = random(16, 32), a = randomStr(o), s = stringChangeASCIINumberArrs(a), 
    l = 0, c = 0, u = 0, h = 0; h < t.length; h++)
        i = t.charCodeAt(h),
        l == pubPassNum.length && (l = 0),
        i += pubPassNum[l],
        l++,
        c == s.length && (c = 0),
        i += s[c],
        c++,
        u += i,
        u > 65535 && (u -= 65535),
        r = i.toString(36),
        r = ("00" + r).substr(-2, 2),
        1 == r.length && (r = "0" + r),
        n.push(r);
    var d = "";
    return d = u.toString(36),
    d = ("0000" + r).substr(-4, 4),
    n.unshift(a),
    n.unshift(o.toString(36)),
    n.unshift(d),
    n.join("")
}
decryptCode = function(e) {
    var t = ""
      , n = 0
      , i = ""
      , r = []
      , o = []
      , a = 0
      , s = 0
    t = e.substr(4, 1),
    n = parseInt(t, 36),
    i = e.substr(5, n),
    r = stringChangeASCIINumberArrs(i),
    pubPass = "BX1o65CoobwcDP33iQW6ld1OyIPsNzF1",
    pubPassNum = stringChangeASCIINumberArrs(pubPass),
    t = e.substr(5 + n, e.length - 5 - n);
    for (var l = "", c = 0, u = 0, h = 0; h < t.length / 2; h++)
        l = t.substr(u, 2),
        u += 2,
        c = parseInt(l, 36),
        s == r.length && (s = 0),
        c -= r[s],
        s++,
        a == pubPass.length && (a = 0),
        c -= pubPassNum[a],
        a++,
        l = String.fromCharCode(c),
        o.push(l);
    t = o.join(""), 
    t = decodeURI(t),
    t = JSON.parse(t);
    return t

}

// console.log(decryptCode(data)['results'][0]['args'][0]['list'])
console.log(encrypt(1))