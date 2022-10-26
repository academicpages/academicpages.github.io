---
layout: none
---

step1list = new Array();
step1list["ΦΑΓΙΑ"] = "ΦΑ";
step1list["ΦΑΓΙΟΥ"] = "ΦΑ";
step1list["ΦΑΓΙΩΝ"] = "ΦΑ";
step1list["ΣΚΑΓΙΑ"] = "ΣΚΑ";
step1list["ΣΚΑΓΙΟΥ"] = "ΣΚΑ";
step1list["ΣΚΑΓΙΩΝ"] = "ΣΚΑ";
step1list["ΟΛΟΓΙΟΥ"] = "ΟΛΟ";
step1list["ΟΛΟΓΙΑ"] = "ΟΛΟ";
step1list["ΟΛΟΓΙΩΝ"] = "ΟΛΟ";
step1list["ΣΟΓΙΟΥ"] = "ΣΟ";
step1list["ΣΟΓΙΑ"] = "ΣΟ";
step1list["ΣΟΓΙΩΝ"] = "ΣΟ";
step1list["ΤΑΤΟΓΙΑ"] = "ΤΑΤΟ";
step1list["ΤΑΤΟΓΙΟΥ"] = "ΤΑΤΟ";
step1list["ΤΑΤΟΓΙΩΝ"] = "ΤΑΤΟ";
step1list["ΚΡΕΑΣ"] = "ΚΡΕ";
step1list["ΚΡΕΑΤΟΣ"] = "ΚΡΕ";
step1list["ΚΡΕΑΤΑ"] = "ΚΡΕ";
step1list["ΚΡΕΑΤΩΝ"] = "ΚΡΕ";
step1list["ΠΕΡΑΣ"] = "ΠΕΡ";
step1list["ΠΕΡΑΤΟΣ"] = "ΠΕΡ";
step1list["ΠΕΡΑΤΑ"] = "ΠΕΡ";
step1list["ΠΕΡΑΤΩΝ"] = "ΠΕΡ";
step1list["ΤΕΡΑΣ"] = "ΤΕΡ";
step1list["ΤΕΡΑΤΟΣ"] = "ΤΕΡ";
step1list["ΤΕΡΑΤΑ"] = "ΤΕΡ";
step1list["ΤΕΡΑΤΩΝ"] = "ΤΕΡ";
step1list["ΦΩΣ"] = "ΦΩ";
step1list["ΦΩΤΟΣ"] = "ΦΩ";
step1list["ΦΩΤΑ"] = "ΦΩ";
step1list["ΦΩΤΩΝ"] = "ΦΩ";
step1list["ΚΑΘΕΣΤΩΣ"] = "ΚΑΘΕΣΤ";
step1list["ΚΑΘΕΣΤΩΤΟΣ"] = "ΚΑΘΕΣΤ";
step1list["ΚΑΘΕΣΤΩΤΑ"] = "ΚΑΘΕΣΤ";
step1list["ΚΑΘΕΣΤΩΤΩΝ"] = "ΚΑΘΕΣΤ";
step1list["ΓΕΓΟΝΟΣ"] = "ΓΕΓΟΝ";
step1list["ΓΕΓΟΝΟΤΟΣ"] = "ΓΕΓΟΝ";
step1list["ΓΕΓΟΝΟΤΑ"] = "ΓΕΓΟΝ";
step1list["ΓΕΓΟΝΟΤΩΝ"] = "ΓΕΓΟΝ";

v = "[ΑΕΗΙΟΥΩ]";
v2 = "[ΑΕΗΙΟΩ]"

function stemWord(w) {
  var stem;
  var suffix;
  var firstch;
  var origword = w;
  test1 = new Boolean(true);

  if(w.length < 4) {
    return w;
  }

  var re;
  var re2;
  var re3;
  var re4;

  re = /(.*)(ΦΑΓΙΑ|ΦΑΓΙΟΥ|ΦΑΓΙΩΝ|ΣΚΑΓΙΑ|ΣΚΑΓΙΟΥ|ΣΚΑΓΙΩΝ|ΟΛΟΓΙΟΥ|ΟΛΟΓΙΑ|ΟΛΟΓΙΩΝ|ΣΟΓΙΟΥ|ΣΟΓΙΑ|ΣΟΓΙΩΝ|ΤΑΤΟΓΙΑ|ΤΑΤΟΓΙΟΥ|ΤΑΤΟΓΙΩΝ|ΚΡΕΑΣ|ΚΡΕΑΤΟΣ|ΚΡΕΑΤΑ|ΚΡΕΑΤΩΝ|ΠΕΡΑΣ|ΠΕΡΑΤΟΣ|ΠΕΡΑΤΑ|ΠΕΡΑΤΩΝ|ΤΕΡΑΣ|ΤΕΡΑΤΟΣ|ΤΕΡΑΤΑ|ΤΕΡΑΤΩΝ|ΦΩΣ|ΦΩΤΟΣ|ΦΩΤΑ|ΦΩΤΩΝ|ΚΑΘΕΣΤΩΣ|ΚΑΘΕΣΤΩΤΟΣ|ΚΑΘΕΣΤΩΤΑ|ΚΑΘΕΣΤΩΤΩΝ|ΓΕΓΟΝΟΣ|ΓΕΓΟΝΟΤΟΣ|ΓΕΓΟΝΟΤΑ|ΓΕΓΟΝΟΤΩΝ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    suffix = fp[2];
    w = stem + step1list[suffix];
    test1 = false;
  }

  re = /^(.+?)(ΑΔΕΣ|ΑΔΩΝ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;

    reg1 = /(ΟΚ|ΜΑΜ|ΜΑΝ|ΜΠΑΜΠ|ΠΑΤΕΡ|ΓΙΑΓΙ|ΝΤΑΝΤ|ΚΥΡ|ΘΕΙ|ΠΕΘΕΡ)$/;

    if(!(reg1.test(w))) {
      w = w + "ΑΔ";
    }
  }

  re2 = /^(.+?)(ΕΔΕΣ|ΕΔΩΝ)$/;

  if(re2.test(w)) {
    var fp = re2.exec(w);
    stem = fp[1];
    w = stem;

    exept2 = /(ΟΠ|ΙΠ|ΕΜΠ|ΥΠ|ΓΗΠ|ΔΑΠ|ΚΡΑΣΠ|ΜΙΛ)$/;

    if(exept2.test(w)) {
      w = w + "ΕΔ";
    }
  }

  re3 = /^(.+?)(ΟΥΔΕΣ|ΟΥΔΩΝ)$/;

  if(re3.test(w)) {
    var fp = re3.exec(w);
    stem = fp[1];
    w = stem;

    exept3 = /(ΑΡΚ|ΚΑΛΙΑΚ|ΠΕΤΑΛ|ΛΙΧ|ΠΛΕΞ|ΣΚ|Σ|ΦΛ|ΦΡ|ΒΕΛ|ΛΟΥΛ|ΧΝ|ΣΠ|ΤΡΑΓ|ΦΕ)$/;

    if(exept3.test(w)) {
      w = w + "ΟΥΔ";
    }
  }

  re4 = /^(.+?)(ΕΩΣ|ΕΩΝ)$/;

  if(re4.test(w)) {
    var fp = re4.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept4 = /^(Θ|Δ|ΕΛ|ΓΑΛ|Ν|Π|ΙΔ|ΠΑΡ)$/;

    if(exept4.test(w)) {
      w = w + "Ε";
    }
  }

  re = /^(.+?)(ΙΑ|ΙΟΥ|ΙΩΝ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    re2 = new RegExp(v + "$");
    test1 = false;

    if(re2.test(w)) {
      w = stem + "Ι";
    }
  }

  re = /^(.+?)(ΙΚΑ|ΙΚΟ|ΙΚΟΥ|ΙΚΩΝ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    re2 = new RegExp(v + "$");
    exept5 = /^(ΑΛ|ΑΔ|ΕΝΔ|ΑΜΑΝ|ΑΜΜΟΧΑΛ|ΗΘ|ΑΝΗΘ|ΑΝΤΙΔ|ΦΥΣ|ΒΡΩΜ|ΓΕΡ|ΕΞΩΔ|ΚΑΛΠ|ΚΑΛΛΙΝ|ΚΑΤΑΔ|ΜΟΥΛ|ΜΠΑΝ|ΜΠΑΓΙΑΤ|ΜΠΟΛ|ΜΠΟΣ|ΝΙΤ|ΞΙΚ|ΣΥΝΟΜΗΛ|ΠΕΤΣ|ΠΙΤΣ|ΠΙΚΑΝΤ|ΠΛΙΑΤΣ|ΠΟΣΤΕΛΝ|ΠΡΩΤΟΔ|ΣΕΡΤ|ΣΥΝΑΔ|ΤΣΑΜ|ΥΠΟΔ|ΦΙΛΟΝ|ΦΥΛΟΔ|ΧΑΣ)$/;

    if((exept5.test(w)) || (re2.test(w))) {
      w = w + "ΙΚ";
    }
  }

  re = /^(.+?)(ΑΜΕ)$/;
  re2 = /^(.+?)(ΑΓΑΜΕ|ΗΣΑΜΕ|ΟΥΣΑΜΕ|ΗΚΑΜΕ|ΗΘΗΚΑΜΕ)$/;
  if(w == "ΑΓΑΜΕ") {
    w = "ΑΓΑΜ";
  }

  if(re2.test(w)) {
    var fp = re2.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;
  }

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept6 = /^(ΑΝΑΠ|ΑΠΟΘ|ΑΠΟΚ|ΑΠΟΣΤ|ΒΟΥΒ|ΞΕΘ|ΟΥΛ|ΠΕΘ|ΠΙΚΡ|ΠΟΤ|ΣΙΧ|Χ)$/;

    if(exept6.test(w)) {
      w = w + "ΑΜ";
    }
  }

  re2 = /^(.+?)(ΑΝΕ)$/;
  re3 = /^(.+?)(ΑΓΑΝΕ|ΗΣΑΝΕ|ΟΥΣΑΝΕ|ΙΟΝΤΑΝΕ|ΙΟΤΑΝΕ|ΙΟΥΝΤΑΝΕ|ΟΝΤΑΝΕ|ΟΤΑΝΕ|ΟΥΝΤΑΝΕ|ΗΚΑΝΕ|ΗΘΗΚΑΝΕ)$/;

  if(re3.test(w)) {
    var fp = re3.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    re3 = /^(ΤΡ|ΤΣ)$/;

    if(re3.test(w)) {
      w = w + "ΑΓΑΝ";
    }
  }

  if(re2.test(w)) {
    var fp = re2.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    re2 = new RegExp(v2 + "$");
    exept7 = /^(ΒΕΤΕΡ|ΒΟΥΛΚ|ΒΡΑΧΜ|Γ|ΔΡΑΔΟΥΜ|Θ|ΚΑΛΠΟΥΖ|ΚΑΣΤΕΛ|ΚΟΡΜΟΡ|ΛΑΟΠΛ|ΜΩΑΜΕΘ|Μ|ΜΟΥΣΟΥΛΜ|Ν|ΟΥΛ|Π|ΠΕΛΕΚ|ΠΛ|ΠΟΛΙΣ|ΠΟΡΤΟΛ|ΣΑΡΑΚΑΤΣ|ΣΟΥΛΤ|ΤΣΑΡΛΑΤ|ΟΡΦ|ΤΣΙΓΓ|ΤΣΟΠ|ΦΩΤΟΣΤΕΦ|Χ|ΨΥΧΟΠΛ|ΑΓ|ΟΡΦ|ΓΑΛ|ΓΕΡ|ΔΕΚ|ΔΙΠΛ|ΑΜΕΡΙΚΑΝ|ΟΥΡ|ΠΙΘ|ΠΟΥΡΙΤ|Σ|ΖΩΝΤ|ΙΚ|ΚΑΣΤ|ΚΟΠ|ΛΙΧ|ΛΟΥΘΗΡ|ΜΑΙΝΤ|ΜΕΛ|ΣΙΓ|ΣΠ|ΣΤΕΓ|ΤΡΑΓ|ΤΣΑΓ|Φ|ΕΡ|ΑΔΑΠ|ΑΘΙΓΓ|ΑΜΗΧ|ΑΝΙΚ|ΑΝΟΡΓ|ΑΠΗΓ|ΑΠΙΘ|ΑΤΣΙΓΓ|ΒΑΣ|ΒΑΣΚ|ΒΑΘΥΓΑΛ|ΒΙΟΜΗΧ|ΒΡΑΧΥΚ|ΔΙΑΤ|ΔΙΑΦ|ΕΝΟΡΓ|ΘΥΣ|ΚΑΠΝΟΒΙΟΜΗΧ|ΚΑΤΑΓΑΛ|ΚΛΙΒ|ΚΟΙΛΑΡΦ|ΛΙΒ|ΜΕΓΛΟΒΙΟΜΗΧ|ΜΙΚΡΟΒΙΟΜΗΧ|ΝΤΑΒ|ΞΗΡΟΚΛΙΒ|ΟΛΙΓΟΔΑΜ|ΟΛΟΓΑΛ|ΠΕΝΤΑΡΦ|ΠΕΡΗΦ|ΠΕΡΙΤΡ|ΠΛΑΤ|ΠΟΛΥΔΑΠ|ΠΟΛΥΜΗΧ|ΣΤΕΦ|ΤΑΒ|ΤΕΤ|ΥΠΕΡΗΦ|ΥΠΟΚΟΠ|ΧΑΜΗΛΟΔΑΠ|ΨΗΛΟΤΑΒ)$/;

    if((re2.test(w)) || (exept7.test(w))) {
      w = w + "ΑΝ";
    }
  }

  re3 = /^(.+?)(ΕΤΕ)$/;
  re4 = /^(.+?)(ΗΣΕΤΕ)$/;

  if(re4.test(w)) {
    var fp = re4.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;
  }

  if(re3.test(w)) {
    var fp = re3.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    re3 = new RegExp(v2 + "$");
    exept8 = /(ΟΔ|ΑΙΡ|ΦΟΡ|ΤΑΘ|ΔΙΑΘ|ΣΧ|ΕΝΔ|ΕΥΡ|ΤΙΘ|ΥΠΕΡΘ|ΡΑΘ|ΕΝΘ|ΡΟΘ|ΣΘ|ΠΥΡ|ΑΙΝ|ΣΥΝΔ|ΣΥΝ|ΣΥΝΘ|ΧΩΡ|ΠΟΝ|ΒΡ|ΚΑΘ|ΕΥΘ|ΕΚΘ|ΝΕΤ|ΡΟΝ|ΑΡΚ|ΒΑΡ|ΒΟΛ|ΩΦΕΛ)$/;
    exept9 = /^(ΑΒΑΡ|ΒΕΝ|ΕΝΑΡ|ΑΒΡ|ΑΔ|ΑΘ|ΑΝ|ΑΠΛ|ΒΑΡΟΝ|ΝΤΡ|ΣΚ|ΚΟΠ|ΜΠΟΡ|ΝΙΦ|ΠΑΓ|ΠΑΡΑΚΑΛ|ΣΕΡΠ|ΣΚΕΛ|ΣΥΡΦ|ΤΟΚ|Υ|Δ|ΕΜ|ΘΑΡΡ|Θ)$/;

    if((re3.test(w)) || (exept8.test(w)) || (exept9.test(w))) {
      w = w + "ΕΤ";
    }
  }

  re = /^(.+?)(ΟΝΤΑΣ|ΩΝΤΑΣ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept10 = /^(ΑΡΧ)$/;
    exept11 = /(ΚΡΕ)$/;
    if(exept10.test(w)) {
      w = w + "ΟΝΤ";
    }
    if(exept11.test(w)) {
      w = w + "ΩΝΤ";
    }
  }

  re = /^(.+?)(ΟΜΑΣΤΕ|ΙΟΜΑΣΤΕ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept11 = /^(ΟΝ)$/;

    if(exept11.test(w)) {
      w = w + "ΟΜΑΣΤ";
    }
  }

  re = /^(.+?)(ΕΣΤΕ)$/;
  re2 = /^(.+?)(ΙΕΣΤΕ)$/;

  if(re2.test(w)) {
    var fp = re2.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    re2 = /^(Π|ΑΠ|ΣΥΜΠ|ΑΣΥΜΠ|ΑΚΑΤΑΠ|ΑΜΕΤΑΜΦ)$/;

    if(re2.test(w)) {
      w = w + "ΙΕΣΤ";
    }
  }

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept12 = /^(ΑΛ|ΑΡ|ΕΚΤΕΛ|Ζ|Μ|Ξ|ΠΑΡΑΚΑΛ|ΑΡ|ΠΡΟ|ΝΙΣ)$/;

    if(exept12.test(w)) {
      w = w + "ΕΣΤ";
    }
  }

  re = /^(.+?)(ΗΚΑ|ΗΚΕΣ|ΗΚΕ)$/;
  re2 = /^(.+?)(ΗΘΗΚΑ|ΗΘΗΚΕΣ|ΗΘΗΚΕ)$/;

  if(re2.test(w)) {
    var fp = re2.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;
  }

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept13 = /(ΣΚΩΛ|ΣΚΟΥΛ|ΝΑΡΘ|ΣΦ|ΟΘ|ΠΙΘ)$/;
    exept14 = /^(ΔΙΑΘ|Θ|ΠΑΡΑΚΑΤΑΘ|ΠΡΟΣΘ|ΣΥΝΘ|)$/;

    if((exept13.test(w)) || (exept14.test(w))) {
      w = w + "ΗΚ";
    }
  }

  re = /^(.+?)(ΟΥΣΑ|ΟΥΣΕΣ|ΟΥΣΕ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept15 = /^(ΦΑΡΜΑΚ|ΧΑΔ|ΑΓΚ|ΑΝΑΡΡ|ΒΡΟΜ|ΕΚΛΙΠ|ΛΑΜΠΙΔ|ΛΕΧ|Μ|ΠΑΤ|Ρ|Λ|ΜΕΔ|ΜΕΣΑΖ|ΥΠΟΤΕΙΝ|ΑΜ|ΑΙΘ|ΑΝΗΚ|ΔΕΣΠΟΖ|ΕΝΔΙΑΦΕΡ|ΔΕ|ΔΕΥΤΕΡΕΥ|ΚΑΘΑΡΕΥ|ΠΛΕ|ΤΣΑ)$/;
    exept16 = /(ΠΟΔΑΡ|ΒΛΕΠ|ΠΑΝΤΑΧ|ΦΡΥΔ|ΜΑΝΤΙΛ|ΜΑΛΛ|ΚΥΜΑΤ|ΛΑΧ|ΛΗΓ|ΦΑΓ|ΟΜ|ΠΡΩΤ)$/;

    if((exept15.test(w)) || (exept16.test(w))) {
      w = w + "ΟΥΣ";
    }
  }

  re = /^(.+?)(ΑΓΑ|ΑΓΕΣ|ΑΓΕ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept17 = /^(ΨΟΦ|ΝΑΥΛΟΧ)$/;
    exept20 = /(ΚΟΛΛ)$/;
    exept18 = /^(ΑΒΑΣΤ|ΠΟΛΥΦ|ΑΔΗΦ|ΠΑΜΦ|Ρ|ΑΣΠ|ΑΦ|ΑΜΑΛ|ΑΜΑΛΛΙ|ΑΝΥΣΤ|ΑΠΕΡ|ΑΣΠΑΡ|ΑΧΑΡ|ΔΕΡΒΕΝ|ΔΡΟΣΟΠ|ΞΕΦ|ΝΕΟΠ|ΝΟΜΟΤ|ΟΛΟΠ|ΟΜΟΤ|ΠΡΟΣΤ|ΠΡΟΣΩΠΟΠ|ΣΥΜΠ|ΣΥΝΤ|Τ|ΥΠΟΤ|ΧΑΡ|ΑΕΙΠ|ΑΙΜΟΣΤ|ΑΝΥΠ|ΑΠΟΤ|ΑΡΤΙΠ|ΔΙΑΤ|ΕΝ|ΕΠΙΤ|ΚΡΟΚΑΛΟΠ|ΣΙΔΗΡΟΠ|Λ|ΝΑΥ|ΟΥΛΑΜ|ΟΥΡ|Π|ΤΡ|Μ)$/;
    exept19 = /(ΟΦ|ΠΕΛ|ΧΟΡΤ|ΛΛ|ΣΦ|ΡΠ|ΦΡ|ΠΡ|ΛΟΧ|ΣΜΗΝ)$/;

    if(((exept18.test(w)) || (exept19.test(w))) && !((exept17.test(w)) || (exept20.test(w)))) {
      w = w + "ΑΓ";
    }
  }

  re = /^(.+?)(ΗΣΕ|ΗΣΟΥ|ΗΣΑ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept21 = /^(Ν|ΧΕΡΣΟΝ|ΔΩΔΕΚΑΝ|ΕΡΗΜΟΝ|ΜΕΓΑΛΟΝ|ΕΠΤΑΝ)$/;

    if(exept21.test(w)) {
      w = w + "ΗΣ";
    }
  }

  re = /^(.+?)(ΗΣΤΕ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept22 = /^(ΑΣΒ|ΣΒ|ΑΧΡ|ΧΡ|ΑΠΛ|ΑΕΙΜΝ|ΔΥΣΧΡ|ΕΥΧΡ|ΚΟΙΝΟΧΡ|ΠΑΛΙΜΨ)$/;

    if(exept22.test(w)) {
      w = w + "ΗΣΤ";
    }
  }

  re = /^(.+?)(ΟΥΝΕ|ΗΣΟΥΝΕ|ΗΘΟΥΝΕ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept23 = /^(Ν|Ρ|ΣΠΙ|ΣΤΡΑΒΟΜΟΥΤΣ|ΚΑΚΟΜΟΥΤΣ|ΕΞΩΝ)$/;

    if(exept23.test(w)) {
      w = w + "ΟΥΝ";
    }
  }

  re = /^(.+?)(ΟΥΜΕ|ΗΣΟΥΜΕ|ΗΘΟΥΜΕ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
    test1 = false;

    exept24 = /^(ΠΑΡΑΣΟΥΣ|Φ|Χ|ΩΡΙΟΠΛ|ΑΖ|ΑΛΛΟΣΟΥΣ|ΑΣΟΥΣ)$/;

    if(exept24.test(w)) {
      w = w + "ΟΥΜ";
    }
  }

  re = /^(.+?)(ΜΑΤΑ|ΜΑΤΩΝ|ΜΑΤΟΣ)$/;
  re2 = /^(.+?)(Α|ΑΓΑΤΕ|ΑΓΑΝ|ΑΕΙ|ΑΜΑΙ|ΑΝ|ΑΣ|ΑΣΑΙ|ΑΤΑΙ|ΑΩ|Ε|ΕΙ|ΕΙΣ|ΕΙΤΕ|ΕΣΑΙ|ΕΣ|ΕΤΑΙ|Ι|ΙΕΜΑΙ|ΙΕΜΑΣΤΕ|ΙΕΤΑΙ|ΙΕΣΑΙ|ΙΕΣΑΣΤΕ|ΙΟΜΑΣΤΑΝ|ΙΟΜΟΥΝ|ΙΟΜΟΥΝΑ|ΙΟΝΤΑΝ|ΙΟΝΤΟΥΣΑΝ|ΙΟΣΑΣΤΑΝ|ΙΟΣΑΣΤΕ|ΙΟΣΟΥΝ|ΙΟΣΟΥΝΑ|ΙΟΤΑΝ|ΙΟΥΜΑ|ΙΟΥΜΑΣΤΕ|ΙΟΥΝΤΑΙ|ΙΟΥΝΤΑΝ|Η|ΗΔΕΣ|ΗΔΩΝ|ΗΘΕΙ|ΗΘΕΙΣ|ΗΘΕΙΤΕ|ΗΘΗΚΑΤΕ|ΗΘΗΚΑΝ|ΗΘΟΥΝ|ΗΘΩ|ΗΚΑΤΕ|ΗΚΑΝ|ΗΣ|ΗΣΑΝ|ΗΣΑΤΕ|ΗΣΕΙ|ΗΣΕΣ|ΗΣΟΥΝ|ΗΣΩ|Ο|ΟΙ|ΟΜΑΙ|ΟΜΑΣΤΑΝ|ΟΜΟΥΝ|ΟΜΟΥΝΑ|ΟΝΤΑΙ|ΟΝΤΑΝ|ΟΝΤΟΥΣΑΝ|ΟΣ|ΟΣΑΣΤΑΝ|ΟΣΑΣΤΕ|ΟΣΟΥΝ|ΟΣΟΥΝΑ|ΟΤΑΝ|ΟΥ|ΟΥΜΑΙ|ΟΥΜΑΣΤΕ|ΟΥΝ|ΟΥΝΤΑΙ|ΟΥΝΤΑΝ|ΟΥΣ|ΟΥΣΑΝ|ΟΥΣΑΤΕ|Υ|ΥΣ|Ω|ΩΝ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem + "ΜΑ";
  }

  if((re2.test(w)) && (test1)) {
    var fp = re2.exec(w);
    stem = fp[1];
    w = stem;

  }

  re = /^(.+?)(ΕΣΤΕΡ|ΕΣΤΑΤ|ΟΤΕΡ|ΟΤΑΤ|ΥΤΕΡ|ΥΤΑΤ|ΩΤΕΡ|ΩΤΑΤ)$/;

  if(re.test(w)) {
    var fp = re.exec(w);
    stem = fp[1];
    w = stem;
  }

  return w;
};

var greekStemmer = function (token) {
  return token.update(function (word) {
    return stemWord(word);
  })
}

var idx = lunr(function () {
  this.field('title')
  this.field('excerpt')
  this.field('categories')
  this.field('tags')
  this.ref('id')

  this.pipeline.remove(lunr.trimmer)
  this.pipeline.add(greekStemmer)
  this.pipeline.remove(lunr.stemmer)

  for (var item in store) {
    this.add({
      title: store[item].title,
      excerpt: store[item].excerpt,
      categories: store[item].categories,
      tags: store[item].tags,
      id: item
    })
  }
});

$(document).ready(function() {
  $('input#search').on('keyup', function () {
    var resultdiv = $('#results');
    var query = $(this).val().toLowerCase();
    var result =
      idx.query(function (q) {
        query.split(lunr.tokenizer.separator).forEach(function (term) {
          q.term(term, { boost: 100 })
          if(query.lastIndexOf(" ") != query.length-1){
            q.term(term, { usePipeline: false, wildcard: lunr.Query.wildcard.TRAILING, boost: 10 })
          }
          if (term != ""){
            q.term(term, { usePipeline: false, editDistance: 1, boost: 1 })
          }
        })
      });
    resultdiv.empty();
    resultdiv.prepend('<p class="results__found">'+result.length+' {{ site.data.ui-text[site.locale].results_found | default: "Result(s) found" }}</p>');
    for (var item in result) {
      var ref = result[item].ref;
      if(store[ref].teaser){
        var searchitem =
          '<div class="list__item">'+
            '<article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">'+
              '<h2 class="archive__item-title" itemprop="headline">'+
                '<a href="'+store[ref].url+'" rel="permalink">'+store[ref].title+'</a>'+
              '</h2>'+
              '<div class="archive__item-teaser">'+
                '<img src="'+store[ref].teaser+'" alt="">'+
              '</div>'+
              '<p class="archive__item-excerpt" itemprop="description">'+store[ref].excerpt.split(" ").splice(0,20).join(" ")+'...</p>'+
            '</article>'+
          '</div>';
      }
      else{
    	  var searchitem =
          '<div class="list__item">'+
            '<article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">'+
              '<h2 class="archive__item-title" itemprop="headline">'+
                '<a href="'+store[ref].url+'" rel="permalink">'+store[ref].title+'</a>'+
              '</h2>'+
              '<p class="archive__item-excerpt" itemprop="description">'+store[ref].excerpt.split(" ").splice(0,20).join(" ")+'...</p>'+
            '</article>'+
          '</div>';
      }
      resultdiv.append(searchitem);
    }
  });
});
