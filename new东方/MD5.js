// 32 crypto js 
const crypto = require('crypto-js');
    // Start Generation Here
    function hex_md5(input) {
        return crypto.MD5(input).toString();
    }

t = new Date().getTime()

// console.log(hex_md5('appId=5053&t='+ t + '&cityCode=310100&pageIndex=1&pageSize=12&categoryCode=123&order=0750F82C2-D8F6-49F6-878C-1E7EBEBC8DA2'));