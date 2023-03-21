function* FindProxyForURL(url, host) {
    if (yield isHostInAnySubnet(host, [
            '10.1.2.0',
            '10.1.3.0'
        ], '255.255.255.0')) {
        return 'HTTPS proxy.example.com';
    }
    if (yield isHostInAnySubnet(host, [
            '10.2.2.0',
            '10.2.3.0'
        ], '255.255.255.0')) {
        return 'HTTPS proxy.example.com';
    }
    return 'DIRECT';
}
function* isHostInAnySubnet(host, subnets, mask) {
    var subnets_length = subnets.length;
    for (i = 0; i < subnets_length; i++) {
        if (yield isInNet(host, subnets[i], mask)) {
            return true;
        }
    }
}
