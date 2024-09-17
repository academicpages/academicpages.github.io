{
  activesupport = {
    dependencies = ["base64" "bigdecimal" "concurrent-ruby" "connection_pool" "drb" "i18n" "logger" "minitest" "securerandom" "tzinfo"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "094cv9kxa8hwlsw3c0njkvvayd0wszcz9b6xywv4yajrg83zlmvm";
      type = "gem";
    };
    version = "7.2.1";
  };
  addressable = {
    dependencies = ["public_suffix"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0cl2qpvwiffym62z991ynks7imsm87qmgxf0yfsmlwzkgi9qcaa6";
      type = "gem";
    };
    version = "2.8.7";
  };
  base64 = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "01qml0yilb9basf7is2614skjp8384h2pycfx86cr8023arfj98g";
      type = "gem";
    };
    version = "0.2.0";
  };
  bigdecimal = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1gi7zqgmqwi5lizggs1jhc3zlwaqayy9rx2ah80sxy24bbnng558";
      type = "gem";
    };
    version = "3.1.8";
  };
  coffee-script = {
    dependencies = ["coffee-script-source" "execjs"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0rc7scyk7mnpfxqv5yy4y5q1hx3i7q3ahplcp4bq2g5r24g2izl2";
      type = "gem";
    };
    version = "2.4.1";
  };
  coffee-script-source = {
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1907v9q1zcqmmyqzhzych5l7qifgls2rlbnbhy5vzyr7i7yicaz1";
      type = "gem";
    };
    version = "1.12.2";
  };
  colorator = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0f7wvpam948cglrciyqd798gdc6z3cfijciavd0dfixgaypmvy72";
      type = "gem";
    };
    version = "1.1.0";
  };
  commonmarker = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1lb5slzbqrca49h0gaifg82xky5r7i9xgm4560pin1xl5fp15lzx";
      type = "gem";
    };
    version = "0.23.10";
  };
  concurrent-ruby = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0chwfdq2a6kbj6xz9l6zrdfnyghnh32si82la1dnpa5h75ir5anl";
      type = "gem";
    };
    version = "1.3.4";
  };
  connection_pool = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1x32mcpm2cl5492kd6lbjbaf17qsssmpx9kdyr7z1wcif2cwyh0g";
      type = "gem";
    };
    version = "2.4.1";
  };
  csv = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0zfn40dvgjk1xv1z8l11hr9jfg3jncwsc9yhzsz4l4rivkpivg8b";
      type = "gem";
    };
    version = "3.3.0";
  };
  dnsruby = {
    dependencies = ["simpleidn"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "066dpkgka17fkn5cv7sk2f4jmwb5d1jila1cnhm77cnd01k5mqcm";
      type = "gem";
    };
    version = "1.72.2";
  };
  drb = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0h5kbj9hvg5hb3c7l425zpds0vb42phvln2knab8nmazg2zp5m79";
      type = "gem";
    };
    version = "2.2.1";
  };
  em-websocket = {
    dependencies = ["eventmachine" "http_parser.rb"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1a66b0kjk6jx7pai9gc7i27zd0a128gy73nmas98gjz6wjyr4spm";
      type = "gem";
    };
    version = "0.5.3";
  };
  ethon = {
    dependencies = ["ffi"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "17ix0mijpsy3y0c6ywrk5ibarmvqzjsirjyprpsy3hwax8fdm85v";
      type = "gem";
    };
    version = "0.16.0";
  };
  eventmachine = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0wh9aqb0skz80fhfn66lbpr4f86ya2z5rx6gm5xlfhd05bj1ch4r";
      type = "gem";
    };
    version = "1.2.7";
  };
  execjs = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1yywajqlpjhrj1m43s3lfg3i4lkb6pxwccmwps7qw37ndmphdzg8";
      type = "gem";
    };
    version = "2.9.1";
  };
  faraday = {
    dependencies = ["faraday-net_http" "logger"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "00pd34pnfmij5iw1xv73f6d68zng63wyjhmk7dyi010kmb4x5sp6";
      type = "gem";
    };
    version = "2.11.0";
  };
  faraday-net_http = {
    dependencies = ["net-http"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0rg54k4skaz8z7j358p6pdzc9pr84fjq7sdlpicf7s5ig7vb1rlk";
      type = "gem";
    };
    version = "3.3.0";
  };
  ffi = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "07139870npj59jnl8vmk39ja3gdk3fb5z9vc0lf32y2h891hwqsi";
      type = "gem";
    };
    version = "1.17.0";
  };
  forwardable-extended = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "15zcqfxfvsnprwm8agia85x64vjzr2w0xn9vxfnxzgcv8s699v0v";
      type = "gem";
    };
    version = "2.6.0";
  };
  gemoji = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "06nw5mfscjmpap7f0bc9f2hj6zd4jy3pk1lhs6llx5my1h138i3k";
      type = "gem";
    };
    version = "4.1.0";
  };
  github-pages = {
    dependencies = ["github-pages-health-check" "jekyll" "jekyll-avatar" "jekyll-coffeescript" "jekyll-commonmark-ghpages" "jekyll-default-layout" "jekyll-feed" "jekyll-gist" "jekyll-github-metadata" "jekyll-include-cache" "jekyll-mentions" "jekyll-optional-front-matter" "jekyll-paginate" "jekyll-readme-index" "jekyll-redirect-from" "jekyll-relative-links" "jekyll-remote-theme" "jekyll-sass-converter" "jekyll-seo-tag" "jekyll-sitemap" "jekyll-swiss" "jekyll-theme-architect" "jekyll-theme-cayman" "jekyll-theme-dinky" "jekyll-theme-hacker" "jekyll-theme-leap-day" "jekyll-theme-merlot" "jekyll-theme-midnight" "jekyll-theme-minimal" "jekyll-theme-modernist" "jekyll-theme-primer" "jekyll-theme-slate" "jekyll-theme-tactile" "jekyll-theme-time-machine" "jekyll-titles-from-headings" "jemoji" "kramdown" "kramdown-parser-gfm" "liquid" "mercenary" "minima" "nokogiri" "rouge" "terminal-table" "webrick"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "11r22g1j9x2gjaxjk78z2nm5wkirsjlz8iswwi67wqi7fcyljh1b";
      type = "gem";
    };
    version = "232";
  };
  github-pages-health-check = {
    dependencies = ["addressable" "dnsruby" "octokit" "public_suffix" "typhoeus"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0gc431xd6vwrh1p7pc3gp3xn7sy1w7dr7f95hmz4fqa1b97kv2fz";
      type = "gem";
    };
    version = "1.18.2";
  };
  hawkins = {
    dependencies = ["em-websocket" "jekyll"];
    groups = ["jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1aa059nv8dyxvf5m8fb65xppaxpicm7h3v8x2mk7g4fwhw8z7sih";
      type = "gem";
    };
    version = "2.0.5";
  };
  html-pipeline = {
    dependencies = ["activesupport" "nokogiri"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "180kjksi0sdlqb0aq0bhal96ifwqm25hzb3w709ij55j51qls7ca";
      type = "gem";
    };
    version = "2.14.3";
  };
  "http_parser.rb" = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1gj4fmls0mf52dlr928gaq0c0cb0m3aqa9kaa6l0ikl2zbqk42as";
      type = "gem";
    };
    version = "0.8.0";
  };
  i18n = {
    dependencies = ["concurrent-ruby"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0k31wcgnvcvd14snz0pfqj976zv6drfsnq6x8acz10fiyms9l8nw";
      type = "gem";
    };
    version = "1.14.6";
  };
  jekyll = {
    dependencies = ["addressable" "colorator" "csv" "em-websocket" "i18n" "jekyll-sass-converter" "jekyll-watch" "kramdown" "liquid" "mercenary" "pathutil" "rouge" "safe_yaml" "webrick"];
    groups = ["jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "144dvgqffkkp34763hj0wh1qabd0fq22sx7bk7afgpy73mv3n8f4";
      type = "gem";
    };
    version = "3.10.0";
  };
  jekyll-avatar = {
    dependencies = ["jekyll"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0jzxmfcljfvjz21wls2w5mr2m5qp0mq9c80j009s4m6yq9vn4wza";
      type = "gem";
    };
    version = "0.8.0";
  };
  jekyll-coffeescript = {
    dependencies = ["coffee-script" "coffee-script-source"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "040i6cyv20qmxlpm74kh5hfci8208ja4903yxdv4x0qs0z172kl9";
      type = "gem";
    };
    version = "1.2.2";
  };
  jekyll-commonmark = {
    dependencies = ["commonmarker"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0i281yiwqiim6jzh7b8hgg8zifs5mn1qz1z6f4109kh9zrcfcc8p";
      type = "gem";
    };
    version = "1.4.0";
  };
  jekyll-commonmark-ghpages = {
    dependencies = ["commonmarker" "jekyll" "jekyll-commonmark" "rouge"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "19544wfdcdh52qw76m6ayv6zbdabqv9wdfp1wqjmdr4k6gr24rym";
      type = "gem";
    };
    version = "0.5.1";
  };
  jekyll-default-layout = {
    dependencies = ["jekyll"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1br08grgv7h36jhlvzfaa3ikp1zz4b6s57ak4fhzrsjx997bw9n6";
      type = "gem";
    };
    version = "0.1.5";
  };
  jekyll-feed = {
    dependencies = ["jekyll"];
    groups = ["jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1hzwmjrxi57x68i7jx5rxi8qlcbqcbg3di55wywrp53pr0bap6k8";
      type = "gem";
    };
    version = "0.17.0";
  };
  jekyll-gist = {
    dependencies = ["octokit"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "03wz9j6yq3552nzf4g71qrdm9pfdgbm68abml9sjjgiaan1n8ns9";
      type = "gem";
    };
    version = "1.5.0";
  };
  jekyll-github-metadata = {
    dependencies = ["jekyll" "octokit"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0k2vnq6ns0x3iwnp8pw9lbxds924wmqswzy0gd57f95gpn49kwjc";
      type = "gem";
    };
    version = "2.16.1";
  };
  jekyll-include-cache = {
    dependencies = ["jekyll"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "01d2l6qrmjc42664ns83cv36jbvalcxqbkmj5i22fakka7jvkm67";
      type = "gem";
    };
    version = "0.2.1";
  };
  jekyll-mentions = {
    dependencies = ["html-pipeline" "jekyll"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1n8y67plydfmay3jn865igvgb3h6s2crk8kq7ydk3wmn9h103s1r";
      type = "gem";
    };
    version = "1.6.0";
  };
  jekyll-optional-front-matter = {
    dependencies = ["jekyll"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "06vnxcmgkxm5nvrpv89qq0afjlxmadv63nh4ryglcwhlf4fhdp7c";
      type = "gem";
    };
    version = "0.3.2";
  };
  jekyll-paginate = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0r7bcs8fq98zldih4787zk5i9w24nz5wa26m84ssja95n3sas2l8";
      type = "gem";
    };
    version = "1.1.0";
  };
  jekyll-readme-index = {
    dependencies = ["jekyll"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0chybr1zgnrmc7zf6psszcqnlrcy2jar8h77kci51lxj8vgc8k6p";
      type = "gem";
    };
    version = "0.3.0";
  };
  jekyll-redirect-from = {
    dependencies = ["jekyll"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1nz6kd6qsa160lmjmls4zgx7fwcpp8ac07mpzy80z6zgd7jwldb6";
      type = "gem";
    };
    version = "0.16.0";
  };
  jekyll-relative-links = {
    dependencies = ["jekyll"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0vfx90ajxyj24lz406k3pqknlbzy8nqs7wpz0in4ps9rggsh24yi";
      type = "gem";
    };
    version = "0.6.1";
  };
  jekyll-remote-theme = {
    dependencies = ["addressable" "jekyll" "jekyll-sass-converter" "rubyzip"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0h2bwl42dig0282366kpxazxb8xafnppnd4yvq2dzcsg90kfgzfk";
      type = "gem";
    };
    version = "0.4.3";
  };
  jekyll-sass-converter = {
    dependencies = ["sass"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "008ikh5fk0n6ri54mylcl8jn0mq8p2nfyfqif2q3pp0lwilkcxsk";
      type = "gem";
    };
    version = "1.5.2";
  };
  jekyll-seo-tag = {
    dependencies = ["jekyll"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0638mqhqynghnlnaz0xi1kvnv53wkggaq94flfzlxwandn8x2biz";
      type = "gem";
    };
    version = "2.8.0";
  };
  jekyll-sitemap = {
    dependencies = ["jekyll"];
    groups = ["jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0622rwsn5i0m5xcyzdn86l68wgydqwji03lqixdfm1f1xdfqrq0d";
      type = "gem";
    };
    version = "1.4.0";
  };
  jekyll-swiss = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "18w893f2snpbvgl80jnmq3xxsl5yi5a5qm11iy3gx0d8viasi6f2";
      type = "gem";
    };
    version = "1.0.0";
  };
  jekyll-theme-architect = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0h04zxlcdsb73qxh08xmsc36gmj95plwxr9g5zwzqd3bmbfd6xbj";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-cayman = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0ajzhqhnj8gc5ns7i69kh69mzidvxkjs7yblrhzb13iaqzwi8prw";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-dinky = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0z1clccf4q0g2zzhl1hfy3x2rcdjs6bzs9ab76lkmpphj5q2a2vj";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-hacker = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "12ppp0bxffy838p4my79nppq112fazifr3cxwvhv3l6yjbwzjsw1";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-leap-day = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1lf7bbpr2s2rir2nf07rnh2g9mjy6zidpacs3j45la70b8qah7lj";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-merlot = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0ifmvq44vwmkp6sb79ys8lx5w24gn3dhdr32bg562da2c8dv5wnb";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-midnight = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1plindxr5vrk98frzxbnkashgnqs86xkg26rjmhgz0qf6mkz77q0";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-minimal = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "10idwpbqjqfc5i895ijf74ac79lccxpz30bvwp4x4fjp6l6229d2";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-modernist = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1kzvdnk1vw8y6x8gy340mhnxipxh9p1h1h20br68clyxbsy7brsb";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-primer = {
    dependencies = ["jekyll" "jekyll-github-metadata" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1cq7lfwa3xs8hkx3cmv2ics7cr4r2azv66m0gfav0zi1k0kjh9yf";
      type = "gem";
    };
    version = "0.6.0";
  };
  jekyll-theme-slate = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0f9l7kaafab2cphkx8gh4b12d8zzbg2ig7x2qzxvxfqjwyfr0h2y";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-tactile = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0li64hnjp4qw7fwsdx0767z7mwxn3kri6sqlg9fkicnmmr41p1mp";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-theme-time-machine = {
    dependencies = ["jekyll" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1qjgsw2n3zny345h540n6rm9600mad7rs33qf6k4rhngxjkr0d5w";
      type = "gem";
    };
    version = "0.2.0";
  };
  jekyll-titles-from-headings = {
    dependencies = ["jekyll"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "10c4sa3gwyidmkcs8h6223lmqpw3h09mn7w8hxfppsk1wda6fdkp";
      type = "gem";
    };
    version = "0.5.3";
  };
  jekyll-watch = {
    dependencies = ["listen"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1qd7hy1kl87fl7l0frw5qbn22x7ayfzlv9a5ca1m59g0ym1ysi5w";
      type = "gem";
    };
    version = "2.2.1";
  };
  jemoji = {
    dependencies = ["gemoji" "html-pipeline" "jekyll"];
    groups = ["jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0z4yabsvqdb8x1rr60yyzbaf950cyzv984n3jwwvgcmv5j73wk2x";
      type = "gem";
    };
    version = "0.13.0";
  };
  kramdown = {
    dependencies = ["rexml"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1ic14hdcqxn821dvzki99zhmcy130yhv5fqfffkcf87asv5mnbmn";
      type = "gem";
    };
    version = "2.4.0";
  };
  kramdown-parser-gfm = {
    dependencies = ["kramdown"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0a8pb3v951f4x7h968rqfsa19c8arz21zw1vaj42jza22rap8fgv";
      type = "gem";
    };
    version = "1.1.0";
  };
  liquid = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1czxv2i1gv3k7hxnrgfjb0z8khz74l4pmfwd70c7kr25l2qypksg";
      type = "gem";
    };
    version = "4.0.4";
  };
  listen = {
    dependencies = ["rb-fsevent" "rb-inotify"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0rwwsmvq79qwzl6324yc53py02kbrcww35si720490z5w0j497nv";
      type = "gem";
    };
    version = "3.9.0";
  };
  logger = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0lwncq2rf8gm79g2rcnnyzs26ma1f4wnfjm6gs4zf2wlsdz5in9s";
      type = "gem";
    };
    version = "1.6.1";
  };
  mercenary = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "10la0xw82dh5mqab8bl0dk21zld63cqxb1g16fk8cb39ylc4n21a";
      type = "gem";
    };
    version = "0.3.6";
  };
  mini_portile2 = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1q1f2sdw3y3y9mnym9dhjgsjr72sq975cfg5c4yx7gwv8nmzbvhk";
      type = "gem";
    };
    version = "2.8.7";
  };
  minima = {
    dependencies = ["jekyll" "jekyll-feed" "jekyll-seo-tag"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1gk7jmriiswda1ykjzpsw9cpiya4m9n0yrh0h6xnrc8zcfy543jj";
      type = "gem";
    };
    version = "2.5.1";
  };
  minitest = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1n1akmc6bibkbxkzm1p1wmfb4n9vv397knkgz0ffykb3h1d7kdix";
      type = "gem";
    };
    version = "5.25.1";
  };
  net-http = {
    dependencies = ["uri"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "10n2n9aq00ih8v881af88l1zyrqgs5cl3njdw8argjwbl5ggqvm9";
      type = "gem";
    };
    version = "0.4.1";
  };
  nokogiri = {
    dependencies = ["mini_portile2" "racc"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "15gysw8rassqgdq3kwgl4mhqmrgh7nk2qvrcqp4ijyqazgywn6gq";
      type = "gem";
    };
    version = "1.16.7";
  };
  octokit = {
    dependencies = ["faraday" "sawyer"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "15lvy06h276jryxg19258b2yqaykf0567sp0n16yipywhbp94860";
      type = "gem";
    };
    version = "4.25.1";
  };
  pathutil = {
    dependencies = ["forwardable-extended"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "12fm93ljw9fbxmv2krki5k5wkvr7560qy8p4spvb9jiiaqv78fz4";
      type = "gem";
    };
    version = "0.16.2";
  };
  public_suffix = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1vb6f3v8q9m67xmbdl4vbmxis53a7igci4blg561jdfp613cf3i5";
      type = "gem";
    };
    version = "5.1.1";
  };
  racc = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0byn0c9nkahsl93y9ln5bysq4j31q8xkf2ws42swighxd4lnjzsa";
      type = "gem";
    };
    version = "1.8.1";
  };
  rb-fsevent = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1zmf31rnpm8553lqwibvv3kkx0v7majm1f341xbxc0bk5sbhp423";
      type = "gem";
    };
    version = "0.11.2";
  };
  rb-inotify = {
    dependencies = ["ffi"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0vmy8xgahixcz6hzwy4zdcyn2y6d6ri8dqv5xccgzc1r292019x0";
      type = "gem";
    };
    version = "0.11.1";
  };
  rexml = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "09shc1dvg88c4yx83d4c9wf26z838nlapa3cmlq8iqdci39a98v2";
      type = "gem";
    };
    version = "3.3.7";
  };
  rouge = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1dnfkrk8xx2m8r3r9m2p5xcq57viznyc09k7r3i4jbm758i57lx3";
      type = "gem";
    };
    version = "3.30.0";
  };
  rubyzip = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0grps9197qyxakbpw02pda59v45lfgbgiyw48i0mq9f2bn9y6mrz";
      type = "gem";
    };
    version = "2.3.2";
  };
  safe_yaml = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0j7qv63p0vqcd838i2iy2f76c3dgwzkiz1d1xkg7n0pbnxj2vb56";
      type = "gem";
    };
    version = "1.0.5";
  };
  sass = {
    dependencies = ["sass-listen"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0p95lhs0jza5l7hqci1isflxakz83xkj97lkvxl919is0lwhv2w0";
      type = "gem";
    };
    version = "3.7.4";
  };
  sass-listen = {
    dependencies = ["rb-fsevent" "rb-inotify"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0xw3q46cmahkgyldid5hwyiwacp590zj2vmswlll68ryvmvcp7df";
      type = "gem";
    };
    version = "4.0.0";
  };
  sawyer = {
    dependencies = ["addressable" "faraday"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1jks1qjbmqm8f9kvwa81vqj39avaj9wdnzc531xm29a55bb74fps";
      type = "gem";
    };
    version = "0.9.2";
  };
  securerandom = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1phv6kh417vkanhssbjr960c0gfqvf8z7d3d9fd2yvd41q64bw4q";
      type = "gem";
    };
    version = "0.3.1";
  };
  simpleidn = {
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0a9c1mdy12y81ck7mcn9f9i2s2wwzjh1nr92ps354q517zq9dkh8";
      type = "gem";
    };
    version = "0.2.3";
  };
  terminal-table = {
    dependencies = ["unicode-display_width"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1512cngw35hsmhvw4c05rscihc59mnj09m249sm9p3pik831ydqk";
      type = "gem";
    };
    version = "1.8.0";
  };
  typhoeus = {
    dependencies = ["ethon"];
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "0z7gamf6s83wy0yqms3bi4srirn3fc0lc7n65lqanidxcj1xn5qw";
      type = "gem";
    };
    version = "1.4.1";
  };
  tzinfo = {
    dependencies = ["concurrent-ruby"];
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "16w2g84dzaf3z13gxyzlzbf748kylk5bdgg3n1ipvkvvqy685bwd";
      type = "gem";
    };
    version = "2.0.6";
  };
  unicode-display_width = {
    groups = ["default" "jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "1204c1jx2g89pc25qk5150mk7j5k90692i7ihgfzqnad6qni74h2";
      type = "gem";
    };
    version = "1.8.0";
  };
  uri = {
    groups = ["default"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "07ndgxyhzd02cg94s6rnfhkb9rwx9z72lzk368sa9j78wc9qnbfz";
      type = "gem";
    };
    version = "0.13.1";
  };
  webrick = {
    groups = ["jekyll_plugins"];
    platforms = [];
    source = {
      remotes = ["https://rubygems.org"];
      sha256 = "13qm7s0gr2pmfcl7dxrmq38asaza4w0i2n9my4yzs499j731wh8r";
      type = "gem";
    };
    version = "1.8.1";
  };
}
