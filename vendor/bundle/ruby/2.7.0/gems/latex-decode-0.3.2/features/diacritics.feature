Feature: Decode LaTeX diacritics
	As a hacker who works with LaTeX
	I want to be able to decode LaTeX diacritics
	
	Scenario Outline: LaTeX to Unicode transformation
		When I decode the string '<latex>'
		Then the result should be '<unicode>'

	Scenarios: Diacritics
		| latex   | unicode | description                                  |
		| \\\`{o} | ò       | grave accent                                 |
		| \\\'{o} | ó       | acute accent                                 |
		| \\^{o}  | ô       | circumflex                                   |
		| \\"{o}  | ö       | umlaut or dieresis                           |
		| \\H{o}  | ő       | long Hungarian umlaut (double acute)         |
		| \\~{o}  | õ       | tilde                                        |
		| \\c{c}  | ç       | cedilla                                      |
		| \\c c   | ç       |                                              |
		| \\c cb  | çb      |                                              |
		| \\c {cb}| \\c cb  |                                              |
		| \\c C   | Ç       |                                              |
		| {\\c c} | ç       |                                              |
		| \\k{a}  | ą       | ogonek                                       |
		| \\l     | ł       | l with stroke                                |
		| \\L     | Ł       | l with stroke                                |
		| \\={o}  | ō       | macron accent (a bar over the letter)        |
		| \\b{o}  | o̱      | bar under the letter                         |
		| \\.{o}  | ȯ       | dot over the letter                          |
		| \\d{u}  | ụ       | dot under the letter                         |
		| \\r{a}  | å       | ring over the letter                         |
		| \\u{o}  | ŏ       | breve over the letter                        |
		| \\v{s}  | š       | caron/hacek ("v") over the letter            |
		| \\t{oo} | o͡o     | "tie" (inverted u) over the two letters      |
		| \\aa    | å       | ring over the letter a                       |
		| \\AA    | Å       | ring over the letter A                       |
		| \\o     | ø       | slashed o                                    |
		| \\O     | Ø       | slashed O                                    |
		| \\ae    | æ       | ae                                           |
		| \\AE    | Æ       | AE                                           |
	