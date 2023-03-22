safe_tests = [
    "<p>Hi there</p>",
    '<h1 class="foo">Hi There!</h1>',
    '<a data-cite="foo">citation</a>',
    '<div><span>Hi There</span></div>',
];

unsafe_tests = [
    "<script>alert(999);</script>",
    '<a onmouseover="alert(999)">999</a>',
    '<a onmouseover=alert(999)>999</a>',
    '<IMG """><SCRIPT>alert("XSS")</SCRIPT>">',
    '<IMG SRC=# onmouseover="alert(999)">',
    '<<SCRIPT>alert(999);//<</SCRIPT>',
    '<SCRIPT SRC=http://ha.ckers.org/xss.js?< B >',
    '<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K">',
    '<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert(999);">',
    '<IFRAME SRC="javascript:alert(999);"></IFRAME>',
    '<IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>',
    '<EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>',
    // CSS is scrubbed
    '<style src="http://untrusted/style.css"></style>',
    '<style>div#notebook { background-color: alert-red; }</style>',
    '<div style="background-color: alert-red;"></div>',
];

var truncate = function (s, n) {
    // truncate a string with an ellipsis
    if (s.length > n) {
        return s.substr(0, n-3) + '...';
    } else {
        return s;
    }
};

casper.notebook_test(function () {
    this.each(safe_tests, function (self, item) {
        var sanitized = self.evaluate(function (item) {
            return IPython.security.sanitize_html(item);
        }, item);
        
        // string equality may be too strict, but it works for now
        this.test.assertEquals(sanitized, item, "Safe: '" + truncate(item, 32) + "'");
    });
    
    this.each(unsafe_tests, function (self, item) {
        var sanitized = self.evaluate(function (item) {
            return IPython.security.sanitize_html(item);
        }, item);
        
        this.test.assertNotEquals(sanitized, item, 
            "Sanitized: '" + truncate(item, 32) + 
            "' => '" + truncate(sanitized, 32) + "'"
        );
        this.test.assertEquals(sanitized.indexOf("alert"), -1, "alert removed");
    });
});