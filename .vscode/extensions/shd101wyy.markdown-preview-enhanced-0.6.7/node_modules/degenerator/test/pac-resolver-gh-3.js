// FindProxyForURL, isInNet
function FindProxyForURL(url, host) {
    if (isHostInAnySubnet(host, ['10.1.2.0', '10.1.3.0'], '255.255.255.0')) {
        return "HTTPS proxy.example.com";
    }

    if (isHostInAnySubnet(host, ['10.2.2.0', '10.2.3.0'], '255.255.255.0')) {
        return "HTTPS proxy.example.com";
    }

    // Everything else, go direct:
    return "DIRECT";
}

// Checks if the single host is within a list of subnets using the single mask.
function isHostInAnySubnet(host, subnets, mask) {
    var subnets_length = subnets.length;
    for (i = 0; i < subnets_length; i++) {
        if (isInNet(host, subnets[i], mask)) {
            return true;
        }
    }
}
