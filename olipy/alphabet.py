# encoding: utf-8
"""Thematic collections of Unicode glyphs.

This is used by gibberish.py.
"""

__all__ = ["Alphabet"]

import unicodedata
import random
from olipy import corpora

CUSTOM_ALPHABETS = {
    "Dice": u"\N{Die Face-1}\N{Die Face-2}\N{Die Face-3}\N{Die Face-4}\N{Die Face-5}\N{Die Face-6}",
    "Completely Circled Alphabetics": u"ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ",
    "Circled Alphabetics": u"⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ",
    "Fullwidth Alphabetics" : u"ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",
    "Bold Alphabetics" : u"𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
    "Italic Alphabetics" : u"𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧",
    "Bold Italic Alphabetics" : u"𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛",
    "Script Alphabetics" : u"𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏",
    "Script Bold Alphabetics" : u"𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",
    "Fraktur Alphabetics" : u"𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷",
    "Doublestruck Alphabetics" : u"𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
    "Fraktur Bold Alphabetics" : u"𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟",
    "Sans Alphabetics" : u"𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓",
    "Sans Bold Alphabetics" : u"𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇",
    "Sans Italic Alphabetics" : u"𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",
    "Sans Bold Italic Alphabetics" : u"𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯",
    "Monospace Alphabetics" : u"𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
    "Alphabetics with Umlaut" : u"ÄB̈C̈D̈ËF̈G̈ḦÏJ̈K̈L̈M̈N̈ÖP̈Q̈R̈S̈T̈ÜV̈ẄẌŸZ̈äb̈c̈d̈ëf̈g̈ḧïj̈k̈l̈m̈n̈öp̈q̈r̈s̈ẗüv̈ẅẍÿz̈",
    "Modifier Alphabetics" : u"ᴬᴮʿᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴻᴼᴾᴿᵀᵁⱽᵂₐᵇᵈᵉᶠᵍʰᶤʲᵏˡᵐᵑᵒᵖʳˢᵗᵤᵛʷˣʸᶻ",
    "Turned Alphabetics": u"ɐqɔpǝɟƃɥıɾʞʃɯuodbɹsʇnʌʍxʎz",
    "Subscript Alphabetics": u"ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘʀꜱᴛᴜᴠᴡʏᴢₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ",
    "Superscript Alphabetics": u"ᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁⱽᵂᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ",
    "Superscript and Subscript Math" : u"₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾",
    "Filled Circled Numerics": u"➊➋➌➍➎➏➐➑➒",
    "Double Circled Numerics": u"⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾",
    "Empty Circled Numerics": u"①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳",
    "Circled Alphanumerics": u"①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ⓪⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾❶❷❸❹❺❻❼❽❾❿➀➁➂➃➄➅➆➇➈➉➊➋➌➍➎➏➐➑➒➓㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿♳♴♵♶♷♸♹⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾",
    "Stars": u"✢✣✤✥✦✧✨✩✪✫✬✭✮✯✰✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋*͙⁎⁑⃰∗⊛⧆﹡＊٭≛⋆⍟⍣★☆☪⚝✡✦✧⭐⭑⭒",
    "Symbology": u"☀☁☂☃☄★☆☎☏☔☕☚☛☠☢☤☭☮☯☹☺☻☼♫⚐⚑⚒⚓⚔⚕⚖♻✄✌✍✏♀♂⌚",
    "Crossouts": u"Xxˣ͓̽ͯᶍẊẋẌẍₓ⒳Ⓧⓧ☒✕✖✗✘Ｘｘ𝁪𝅃𝅅𝐗𝐱𝑋𝑥𝑿𝒙𝒳𝓍𝓧𝔁𝔛𝔵𝕏𝕩𝖃𝖝𝖷𝗑𝗫𝘅𝘟𝘹𝙓𝙭𝚇𝚡×⨯ⵝ᙭Ҳ⚔⤧ҳ⤩᙮ⅹⅩ⤨⤪⨉⤫⤬",
    "Box Drawing All": u"─━│┃┄┅┆┇┈┉┊┋┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋╌╍╎╏═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╵╶╷╸╹╺╻╼╽╾╿",
    "Box Drawing Double": u"═║╔╗╚╝╠╣╦╩╬",
    "Box Drawing Dots": u"┄┅┆┇┈┉┊┋╍╌╎╏",
    "Box Drawing Thick and Thin": u"┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋╸╹╺╻╼╽╾╿",

    "Box Drawing Single and Double": u"┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╴╵╶╷",
    "Block Drawing by Height": u"▀▁▂▃▄▅▆▇█▔",
    "Block Drawing by Width": u"█▉▊▋▌▍▎▏▐▕",
    "Skin Tones" : u"🏻🏼🏽🏾🏿",
 }

class Alphabet:

    @classmethod
    def default(cls):
        """Load some interesting alphabets."""
        cls._fill_by_name(corpora.language.unicode_code_sheets['code_sheets'])
        return cls

    @classmethod
    def _fill_by_name(cls, data=None, add_custom=True):
        for c in data:
            name = c['name']
            if 'characters' in c and len(c['characters']) > 0:
                cls.by_name[name] = c
            if 'child' in c:
                cls._fill_by_name(c['child'], False)

        if not add_custom:
            return

        # Also add in custom alphabets
        for name, chars in CUSTOM_ALPHABETS.items():
            cls.by_name[name] = dict(characters=chars)

        # Add emoji.
        emoji = []
        for i in cls.EMOJI_S:
            emoji += cls.by_name[i]['characters']
        cls.by_name['Emoji'] = dict(characters=emoji)


    by_name = {}

    @classmethod
    def random_choice(cls, *alphabets):
        """A random choice among alphabets"""
        if not alphabets:
            alphabets = list(cls.by_name.keys())
        choice = random.choice(alphabets)
        return cls.characters([choice])

    @classmethod
    def random_choice_no_modifiers(cls, minimum_size=2):
        """A completely random choice among non-modifier alphabets."""
        choice = None
        while choice is None:
            choice = random.choice(list(cls.by_name.keys()))
            if choice in cls.MODIFIERS:
                choice = None
            # print "Choice: %s, len: %s" % (choice, len(cls.characters(choice)))
            if choice is not None:
                chars = cls.characters(choice)
                if len(chars) < minimum_size:
                    choice = None

        return chars

    @classmethod
    def subset(cls, alphabet, how_many_characters=None):
        """A limited subset of an alphabet."""
        full = Alphabet.random_choice_no_modifiers()
        limited = ''
        if not how_many_characters:
            how_many_characters = max(2, int(random.gauss(4, 2)))
        for i in range(how_many_characters):
            limited += random.choice(alphabet)
        return limited

    @classmethod
    def random_whitespace(cls):
        "A whitespace character selected at random."
        return random.choice(cls.WHITESPACE)

    @classmethod
    def random_modifier(cls):
        "A modifier selected at random."
        alphabet = Alphabet.characters(cls.MODIFIERS)
        return random.choice(alphabet)

    @classmethod
    def characters(cls, alphabets):
        char = []
        if not isinstance(alphabets, list):
            alphabets = [alphabets]
        # print "Character lookup for %r" % alphabets
        for alphabet in alphabets:
            # print "Looking up %s" % alphabet
            if isinstance(alphabet, list):
                char.extend(cls.characters(alphabet))
            else:
                try:
                    char.extend(cls.by_name[alphabet]['characters'])
                except Exception as e:
                    # Assume the string is the alphabet itself rather than the name of an alphabet.
                    char.extend(alphabet)
        return ''.join(char)

    # Some combination European alphabets
    ASCII = "Basic Latin (ASCII)"
    LATIN_1 = [ASCII, "Latin-1 Supplement"]
    LATIN_EXTRAS = [
        "Latin Extended-A", "Latin Extended-B",
        "Latin Extended-C", "Latin Extended-D",
        "Latin Extended Additional", "Latin Ligatures"]
    LATIN_FULL = LATIN_1 + LATIN_EXTRAS
    CYRILLIC = ["Cyrillic"]
    CYRILLIC_FULL = ["Cyrillic", "Cyrillic Supplement", "Cyrillic Extended-A", "Cyrillic Extended-B"]

    LATIN_S = [ASCII, LATIN_1, LATIN_FULL, 
               "Circled Alphabetics",
               "Circled Alphanumerics",
               "Bold Alphabetics",
               "Italic Alphabetics",
               "Script Alphabetics",
               "Bold Italic Alphabetics",
               "Script Bold Alphabetics",
               "Fraktur Alphabetics",
               "Doublestruck Alphabetics",
               "Fraktur Bold Alphabetics",
               "Sans Alphabetics",
               "Sans Bold Alphabetics",
               "Sans Italic Alphabetics",
               "Sans Bold Italic Alphabetics",
               "Monospace Alphabetics",
               "Alphabetics with Umlaut",
               "Turned Alphabetics",
               "Subscript Alphabetics",
               "Superscript Alphabetics",
               ]

    CYRILLIC_S = [CYRILLIC, CYRILLIC_FULL]

    # A set of European alphabets.
    EUROPEAN_S = [
        ASCII, LATIN_1, LATIN_FULL, CYRILLIC, CYRILLIC_FULL,
        ["Armenian", "Armenian Ligatures"],
        ["Coptic"],        
        ["Georgian"],
        ["Georgian", "Georgian Supplement"],
        ["Glagolitic"],
        ["Gothic"],
        ["Greek"],
        ["Greek", "Greek Extended"],
        ["Ogham"],
        ["Old Italic"],
        ["Runic"]
        ]

    # Some combination African alphabets.
    ETHIOPIC = ["Ethiopic"]
    ETHIOPIC_FULL = ["Ethiopic", "Ethiopic Supplement", "Ethiopic Extended", "Ethiopic Extended-A"]

    # A set of African alphabets.
    AFRICAN_S = [ETHIOPIC_FULL, "N'Ko", "Osmanya", "Tifinagh", "Vai"]

    # Some combination Middle Eastern alphabets.
    ARABIC = ["Arabic"]
    ARABIC_FULL = ARABIC + ["Arabic Supplement"]
    ARABIC_WITH_PRESENTATION_FORMS = ARABIC + ["Arabic Presentation Forms-B"]
    HEBREW = ["Hebrew"]
    HEBREW_WITH_PRESENTATION_FORMS = HEBREW + ["Hebrew Presentation Forms"]

    # A set of Middle Eastern alphabets.
    MIDDLE_EASTERN_S = [
        ARABIC, ARABIC_FULL, ARABIC_WITH_PRESENTATION_FORMS,
        HEBREW, HEBREW_WITH_PRESENTATION_FORMS,
        "Old Persian",
        "Ugaritic",
        "Phoenician",
        "Syriac"
        ]

    # A set of Central Asian alphabets.
    CENTRAL_ASIAN_S = [
        "Tibetan",
        ]

    # Some combination South Asian alphabets
    DEVANAGARI = ["Devanagari"]
    DEVANAGARI_EXTENDED = DEVANAGARI + ["Devanagari Extended"]

    # A set of South Asian alphabets
    SOUTH_ASIAN_S = [
        DEVANAGARI,
        DEVANAGARI_EXTENDED,
        "Bengali and Assamese",
        "Gujarati",
        "Gurmukhi",
        "Kannada",
        "Malayalam",
        "Oriya",
        "Sinhala",
        "Tamil",
        "Telugu",
        "Thaana"
        ]

    # Some combination Southeast Asian alphabets
    KHMER = ["Khmer"]
    KHMER_WITH_SYMBOLS = KHMER + ["Khmer Symbols"]
    MYANMAR = ["Myanmar"]
    MYANMAR_EXTENDED = MYANMAR + ["Myanmar Extended-A"]

    # A set of Southeast Asian alphabets
    SOUTHEAST_ASIAN_S = [
        KHMER,
        KHMER_WITH_SYMBOLS,
        MYANMAR,
        MYANMAR_EXTENDED,
        "Buginese",
        "Kayah Li",
        "Lao",
        "Tai Le",
        "Thai",
        ]

    # A set of Phillipine alphabets
    PHILLIPINE_S = [
        "Hanunoo",
        ]

    # Some combination East Asian alphabets.
    HANGUL_JAMO = ["Hangul Jamo"]
    HANGUL_JAMO_WITH_COMPATIBILITY = HANGUL_JAMO + ["Hangul Compatibility Jamo"]
    KATAKANA = ["Katakana"]
    KATAKANA_ALL = KATAKANA + ["Katakana Phonetic Extensions"]

    # A set of East Asian alphabets
    EAST_ASIAN_S = [
        "Bopomofo",
        "CJK Unified Ideographs (Han)",
        "CJK Compatibility Ideographs",
        # "CJK Radicals  KangXi Radicals", # Name is weird
        "Hangul Syllables",
        "Hiragana",
        HANGUL_JAMO,
        HANGUL_JAMO_WITH_COMPATIBILITY,
        KATAKANA,
        KATAKANA_ALL,
        ]

    # Some combination American alphabets
    UCAS = "Unified Canadian Aboriginal Syllabics"
    UCAS_ALL = ["Unified Canadian Aboriginal Syllabics", "UCAS Extended"]

    # A set of American alphabets
    AMERICAN_S = ["Cherokee",
                  "Deseret",
                  UCAS,
                  UCAS_ALL]

    # All available alphabets that are used to convey human language.
    ALL_LANGUAGE_ALPHABETS_S = (EUROPEAN_S + AFRICAN_S + MIDDLE_EASTERN_S
                                + CENTRAL_ASIAN_S + SOUTH_ASIAN_S
                                + SOUTHEAST_ASIAN_S + PHILLIPINE_S
                                + EAST_ASIAN_S + AMERICAN_S)

    # Ways to modify characters.
    DIACRITICAL = ["Combining Diacritical Marks"]
    DIACRITICAL_FULL = DIACRITICAL + [
        "Combining Diacritical Marks Supplement",
        "Combining Half Marks",
        "Combining Diacritical Marks for Symbols"]
    MODIFIERS = DIACRITICAL_FULL

    # "Weird Twitter" versions of Latin characters
    WEIRD_TWITTER_LATIN = [
        "Fullwidth ASCII Punctuation",
        "Superscripts and Subscripts",
        "Mathematical Alphanumeric Symbols",
        "Letterlike Symbols",
        "Enclosed Alphanumerics",
        "Enclosed Alphanumeric Supplement",
        "Additional Squared Symbols",
        "Control Pictures",
        "Braille Patterns",
        "IPA Extensions",
        "Phonetic Extensions",
        "Phonetic Extensions Supplement",
        "Old Italic",
        "Circled Alphabetics",
        "Circled Alphanumerics",
        "Double Circled Numerics",
        "Bold Alphabetics",
        "Italic Alphabetics",
        "Script Alphabetics",
        "Bold Italic Alphabetics",
        "Script Bold Alphabetics",
        "Fraktur Alphabetics",
        "Doublestruck Alphabetics",
        "Fraktur Bold Alphabetics",
        "Sans Alphabetics",
        "Sans Bold Alphabetics",
        "Sans Italic Alphabetics",
        "Sans Bold Italic Alphabetics",
        "Monospace Alphabetics",
        "Alphabetics with Umlaut",
        ]

    # "Weird Twitter" mixins for Latin characters.
    WEIRD_TWITTER_LATIN_MIXINS = [
        "Alphabetic Presentation Forms",
        "General Punctuation",
        "Latin-1 Punctuation",
        "Small Form Variants",
        "Currency Symbols",
        "Dollar Sign",
        "Yen, Pound and Cent",
        "Rial Sign",
        "Vertical Forms",
        "Number Forms",
        "Fullwidth ASCII Digits",
        "Modifier Tone Letters",
        "Spacing Modifier Letters",
        "CJK Compatibility",
        ]

    # "Weird Twitter" versions of Japanese characters
    WEIRD_TWITTER_JAPANESE = [
        "Halfwidth and Fullwidth Forms",
        "Fullwidth ASCII Digits",
        "Halfwidth Katakana",
        ]

    # "Weird Twitter" mixins for Japanese characters
    WEIRD_TWITTER_JAPANESE_MIXINS = [
        "CJK Compatibility Ideographs",
        "Fullwidth ASCII Punctuation",
        "Vertical Forms",
        "CJK Symbols and Punctuation",
        "CJK Compatibility Forms",
        "Enclosed CJK Letters and Months",
        ]

    # "Weird Twitter" for the Han unification plane
    WEIRD_TWITTER_CJK = [
        "Bopomofo",
        "CJK Compatibility Ideographs",
        "CJK Radicals / KangXi Radicals"
        ]

    # "Weird Twitter" mixins for the Han unification plane
    WEIRD_TWITTER_CJK_MIXINS = WEIRD_TWITTER_JAPANESE_MIXINS + [
        "CJK Compatibility"]

    # "Weird Twitter" math glyphs
    WEIRD_TWITTER_MATH = [
        "Number Forms",
        "Fullwidth ASCII Digits",
        "Superscripts and Subscripts",
        "Superscript and Subscript Math",
        ]

    WEIRD_TWITTER_MATH_MIXINS = [
        "Mathematical Operators",
        "Supplemental Mathematical Operators",
        "Miscellaneous Mathematical Symbols-A",
        "Floors and Ceilings",
        ]

    # Symbolic glyphs
    SYMBOLIC_ALPHABETS = [
        "APL symbols",
        "Miscellaneous Technical",
        "Miscellaneous Symbols And Pictographs",
        "Optical Character Recognition (OCR)",
        "Arrows",
        "Supplemental Arrows-A",
        "Supplemental Arrows-B",
        "Additional Arrows",
        "Dingbats",
        "Emoticons",
        "Musical Symbols",
        "Byzantine Musical Symbols",
        ]

    # Gaming glyphs
    GAMING_ALPHABETS = [
        "Chess, Checkers/Draughts",
        "Dice",
        "Domino Tiles",
        "Japanese Chess",
        "Mahjong Tiles",
        "Playing Cards",
        "Card suits",
        ]

    # Geometric glyphs, and glyphs designed for other purposes that
    # have geometric appeal
    GEOMETRIC_ALPHABETS = [
        "Geometric Shapes",
        # "CJK Compatibility Forms",
        "Additional Shapes",
        "Box Drawing",
        "Block Elements",
        "Braille Patterns",
        "Yijing Mono-, Di- and Trigrams",
        "Stars",
        ]

    # Yijing symbols
    YIJING = [
        "Yijing Mono-, Di- and Trigrams",
        "Yijing Hexagram Symbols",
        "Tai Xuan Jing Symbols",
        ]

    # Small glitchy alphabets that can be tossed in almost anywhere.
    GLITCHES = [
        "Optical Character Recognition (OCR)",
        "Floors and Ceilings",
        "Shading Mosaic", # Custom alphabet
        "One Dot", # Custom alphabet
        "Fill Mosaic", # Custom alphabet
        ]

    # Custom alphabets 
    CUSTOM_S = [
        "Geometric Shapes",
        ["Geometric Shapes", "Arrows"],
        ["Geometric Shapes", "Additional Shapes"],
        ["Geometric Shapes", "Additional Shapes", "Box Drawing", "Block Elements"],
        "Box Drawing",
        "Block Elements",
        ["Box Drawing", "Block Elements"],
        ["Box Drawing", "Block Elements", "Optical Character Recognition (OCR)"],
        "Optical Character Recognition (OCR)",
        "Braille Patterns",
        ["Braille Patterns", "Optical Character Recognition (OCR)"],
        ["Dingbats", "Miscellaneous Symbols"],
        ["Dingbats", "Emoticons", "Miscellaneous Symbols"],
        ["Dingbats", "Emoticons", "Miscellaneous Symbols", "Miscellaneous Symbols and Arrows"],
        ["Basic Latin (ASCII)", "Emoticons"],
        "Chess, Checkers/Draughts",
        "Domino Tiles",
        "Playing Cards",
        "Mahjong Tiles",
        "Dice",
        ["Dice", "Domino Tiles"],
        ["Playing Cards", "Card suits"],
        "Yijing Mono-, Di- and Trigrams",
        "Yijing Hexagram Symbols",
        "Tai Xuan Jing Symbols",
        ["Yijing Mono-, Di- and Trigrams", "Yijing Hexagram Symbols", "Tai Xuan Jing Symbols"],
        ["Yijing Mono-, Di- and Trigrams", "Yijing Hexagram Symbols", "Tai Xuan Jing Symbols", "Braille Patterns", "Optical Character Recognition (OCR)"],
        ["Hiragana", "Katakana"],
        ]

    def unicode_charset(name, *chrs):
        charset = "".join(map(unicodedata.lookup, chrs))
        CUSTOM_ALPHABETS[name] = charset
        return charset

    # Custom alphabets
    UP_POINTING_TRIANGLES = unicode_charset("Up-Pointing Triangles",
        "Apl functional symbol delta stile",
        "Black lower left triangle",
        "Black lower right triangle",
        "Black up-pointing small triangle",
        "Black up-pointing triangle",
        "Canadian syllabics glottal stop",
        "Canadian syllabics i",
        "Combining enclosing upward pointing triangle",
        "Coptic capital letter dalda",
        "Coptic small letter dalda",
        "Cyrillic capital letter closed little yus",
        "Cyrillic small letter little yus",
        "Greek capital letter delta",
        "Increment",
        "Mathematical bold capital delta",
        "Mathematical bold italic capital delta",
        "Minus sign in triangle",
        "Segment",
        "Tifinagh letter yav",
        "Triangle with dot above",
        "Triangle with serifs at bottom",
        "Triangle with underbar",
        "Up-pointing triangle with left half black",
        "Up-pointing triangle with right half black",
        "Lower left triangle",
        "Lower right triangle",
        "White trapezium",
        "White up-pointing small triangle",
        "White up-pointing small triangle",
        "White up-pointing triangle",
        #            "Alchemical symbol for fire",
        )

    DOWN_POINTING_TRIANGLES = unicode_charset("Down-Pointing Triangles",
        "Apl functional symbol del stile",
        "Black down-pointing small triangle",
        "Black down-pointing triangle",
        "Canadian syllabics carrier ru",
        "Canadian syllabics e",
        "Canadian syllabics pe",
        "Down-pointing triangle with left half black",
        "Down-pointing triangle with right half black",
        "For all",
        "Latin capital letter v",
        "Mathematical bold capital v",
        "Mathematical bold italic nabla",
        "Mathematical bold nabla",
        "Mathematical bold small v",
        "Mathematical italic nabla",
        "Mathematical monospace capital v",
        "Mathematical monospace small v",
        "Mathematical sans-serif bold nabla",
        "Mathematical sans-serif capital v",
        "Nabla",
        "Tifinagh letter yadh",
        "Vai symbol kung",
        "White down-pointing small triangle",
        "White down-pointing triangle",
        #            "Alchemical symbol for aquafortis"
        #            "Alchemical symbol for dissolve-2",
        #            "Alchemical symbol for water",
        #            "Greek vocal notation symbol-21",
        #            "Heavy white down-pointing triangle",
        )

    LEFT_POINTING_TRIANGLES = unicode_charset("Left-Pointing Triangles",
        "Apl functional symbol quad less-than",
        "Black left-pointing pointer",
        "Black left-pointing small triangle",
        "Black left-pointing triangle",
        "Canadian syllabics a",
        "Canadian syllabics carrier ra",
        "Canadian syllabics p",
        "Canadian syllabics pa",
        "Normal subgroup of",
        "Spherical angle",
        "Lower right triangle",
        "Upper right triangle",
        "Black upper right triangle",
        "Black lower right triangle",
        "Vai syllable gboo",
        "White left-pointing pointer",
        "White left-pointing small triangle",
        "White left-pointing triangle",
        # "Closed subset",
        # "Greek instrumental notation symbol-38",
        # "Large left triangle operator",
        # "Less-than closed by curve",
        #"Z notation domain antirestriction",
        )

    RIGHT_POINTING_TRIANGLES = unicode_charset("Right-Pointing Triangles",
        "Apl functional symbol quad greater-than",
        "Black lower right triangle",
        "Black right-pointing small triangle",
        "Black right-pointing triangle",
        "Black upper left triangle",
        "Canadian syllabics carrier hwee",
        "Canadian syllabics carrier i",
        "Canadian syllabics carrier re",
        "Canadian syllabics carrier we",
        "Canadian syllabics fo",
        "Canadian syllabics o",
        "Contains as normal subgroup",
        "Greater-than sign",
        "Lower right triangle",
        "Spherical angle opening left",
        "Succeeds",
        "Triangular bullet",
        "Upper left triangle",
        "White right-pointing pointer",
        "White right-pointing small triangle",
        "White right-pointing triangle",
        # "Closed superset",
        # "Conical taper",
        # "Greater-than closed by curve",
        # "Greek instrumental notation symbol-37",
        # "Z notation range antirestriction",
        )

    TRIANGLES = UP_POINTING_TRIANGLES + DOWN_POINTING_TRIANGLES + LEFT_POINTING_TRIANGLES + RIGHT_POINTING_TRIANGLES

    RECTANGLES = unicode_charset("Rectangles",
        "BLACK RECTANGLE", #▬
        "WHITE RECTANGLE", #▭
        "BLACK VERTICAL RECTANGLE", #▮
        "WHITE VERTICAL RECTANGLE", #▯
                            )

    QUADRILATERALS = unicode_charset("Quadrilaterals",
        "Apl functional symbol quad backslash",
        "Apl functional symbol quad slash",
        "Apl functional symbol quad",
        "Apl functional symbol quote quad",
        "Apl functional symbol squish quad",
        "Ballot box",
        "Black large square",
        "Black medium small square",
        "Black medium square",
        "Black parallelogram",
        "Black small square",
        "Black square",
        "Combining enclosing screen",
        "Combining enclosing square",
        "Flatness",
        "Hebrew letter wide final mem",
        "Katakana letter ro",
        "Lower right drop-shadowed white square",
        "Lower right shadowed white square",
        "Square lozenge",
        "Upper right drop-shadowed white square",
        "Upper right shadowed white square",
        "Viewdata square",
        "White large square",
        "White medium small square",
        "White medium square",
        "White parallelogram",
        "White small square",
        "White square with rounded corners",
        "White square",
        "White trapezium",
        "X in a rectangle box",
        #"Square with contoured outline",
        #"Ticket",
        "BALLOT BOX WITH CHECK", #☑
        "BALLOT BOX WITH X", #☒
        "MUSICAL SYMBOL SQUARE NOTEHEAD WHITE", #𝅆
        "MUSICAL SYMBOL SQUARE NOTEHEAD BLACK", #𝅇
        "SQUARE WITH TOP HALF BLACK", #⬒
        "SQUARE WITH BOTTOM HALF BLACK", #⬓
        "SQUARE WITH UPPER RIGHT DIAGONAL HALF BLACK", #⬔
        "SQUARE WITH LOWER LEFT DIAGONAL HALF BLACK", #⬕
        "DOTTED SQUARE", #⬚
        "TWO JOINED SQUARES", #⧉
        "WHITE SQUARE WITH LEFTWARDS TICK", #⟤
        "WHITE SQUARE WITH RIGHTWARDS TICK", #⟥
        "SQUARE WITH LEFT HALF BLACK", #◧
        "SQUARE WITH RIGHT HALF BLACK", #◨
        "SQUARE WITH UPPER LEFT DIAGONAL HALF BLACK", #◩
        "SQUARE WITH LOWER RIGHT DIAGONAL HALF BLACK", #◪
        "WHITE SQUARE CONTAINING BLACK SMALL SQUARE", #▣
        "SQUARE WITH HORIZONTAL FILL", #▤
        "SQUARE WITH VERTICAL FILL", #▥
        "SQUARE WITH ORTHOGONAL CROSSHATCH FILL", #▦
        "SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL", #▧
        "SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL", #▨
        "SQUARE WITH DIAGONAL CROSSHATCH FILL", #▩
        "WHITE SQUARE WITH CENTRE VERTICAL LINE", #⎅
        "SQUARE FOOT", #⏍
        ) + RECTANGLES

    PENTAGONS_AND_LARGER_POLYGONS = unicode_charset("Miscellaneous Polygons",
        "Benzene ring with circle",
        "Benzene ring",
        "Black horizontal ellipse",
        "Black shogi piece",
        "Canadian syllabics carrier tho",
        "House",
        "Software-function symbol",
        "White horizontal ellipse",
        "White shogi piece",
        "BLACK PENTAGON", #⬟
        "WHITE PENTAGON", #⬠
        "WHITE HEXAGON", #⬡
        "BLACK HEXAGON", #⬢
        "HORIZONTAL BLACK HEXAGON", #⬣
        "BLACK RIGHT-POINTING PENTAGON", #⭓
        "WHITE RIGHT-POINTING PENTAGON", #⭔
        # "Chestnut",
        )

    CIRCLES = unicode_charset("Circles",
        "UGARITIC LETTER THANNA", #𐎘
        "HEBREW MARK MASORA CIRCLE", #֯
        "ARABIC END OF AYAH", #۝
        "COMBINING ENCLOSING CIRCLE", #⃝
        "COMBINING ENCLOSING CIRCLE BACKSLASH", #⃠
        "APL FUNCTIONAL SYMBOL CIRCLE STILE", #⌽
        "APL FUNCTIONAL SYMBOL CIRCLE JOT", #⌾
        "APL FUNCTIONAL SYMBOL CIRCLE BACKSLASH", #⍉
        "APL FUNCTIONAL SYMBOL CIRCLE UNDERBAR", #⍜
        "APL FUNCTIONAL SYMBOL CIRCLE STAR", #⍟
        "APL FUNCTIONAL SYMBOL CIRCLE DIAERESIS", #⍥
        "BROKEN CIRCLE WITH NORTHWEST ARROW", #⎋
        "DENTISTRY SYMBOL LIGHT VERTICAL WITH CIRCLE", #⏀
        "DENTISTRY SYMBOL LIGHT DOWN AND HORIZONTAL WITH CIRCLE", #⏁
        "DENTISTRY SYMBOL LIGHT UP AND HORIZONTAL WITH CIRCLE", #⏂
        "BENZENE RING WITH CIRCLE", #⏣
        "BULLSEYE", # ◎
        "WHITE CIRCLE", #○
        "DOTTED CIRCLE", #◌
        "CIRCLE WITH VERTICAL FILL", #◍
        "BLACK CIRCLE", #●
        "CIRCLE WITH LEFT HALF BLACK", #◐
        "CIRCLE WITH RIGHT HALF BLACK", #◑
        "CIRCLE WITH LOWER HALF BLACK", #◒
        "CIRCLE WITH UPPER HALF BLACK", #◓
        "CIRCLE WITH UPPER RIGHT QUADRANT BLACK", #◔
        "CIRCLE WITH ALL BUT UPPER LEFT QUADRANT BLACK", #◕
        "INVERSE WHITE CIRCLE", #◙
        "LARGE CIRCLE", #◯
        "WHITE CIRCLE WITH UPPER LEFT QUADRANT", #◴
        "WHITE CIRCLE WITH LOWER LEFT QUADRANT", #◵
        "WHITE CIRCLE WITH LOWER RIGHT QUADRANT", #◶
        "WHITE CIRCLE WITH UPPER RIGHT QUADRANT", #◷
        "WHITE CIRCLE WITH DOT RIGHT", #⚆
        "WHITE CIRCLE WITH TWO DOTS", #⚇
        "BLACK CIRCLE WITH WHITE DOT RIGHT", #⚈
        "BLACK CIRCLE WITH TWO WHITE DOTS", #⚉
        "MEDIUM WHITE CIRCLE", #⚪
        "MEDIUM BLACK CIRCLE", #⚫
        "MEDIUM SMALL WHITE CIRCLE", #⚬
        "SHADOWED WHITE CIRCLE", #❍
        "ANTICLOCKWISE GAPPED CIRCLE ARROW", #⟲
        "CLOCKWISE GAPPED CIRCLE ARROW", #⟳
        "ANTICLOCKWISE CLOSED CIRCLE ARROW", #⥀
        "CLOCKWISE CLOSED CIRCLE ARROW", #⥁
        "EMPTY SET WITH SMALL CIRCLE ABOVE", #⦲
        "CIRCLE WITH HORIZONTAL BAR", #⦵
        "CIRCLE WITH SMALL CIRCLE TO THE RIGHT", #⧂
        "CIRCLE WITH TWO HORIZONTAL STROKES TO THE RIGHT", #⧃
        "BLACK LARGE CIRCLE", #⬤
        )

    SHAPE_CHARSET_S = [UP_POINTING_TRIANGLES, DOWN_POINTING_TRIANGLES, LEFT_POINTING_TRIANGLES, RIGHT_POINTING_TRIANGLES, PENTAGONS_AND_LARGER_POLYGONS, QUADRILATERALS, CIRCLES]

    ONE_DOT = unicode_charset("One Dot",
        "Braille pattern dots-3",
        "Braille pattern dots-7",
        "Bullet operator",
        "Bullet",
        "Canadian syllabics final middle dot",
        "Canadian syllabics y-cree w",
        "Combining dot above right",
        "Combining dot above",
        "Combining dot below",
        "Dot above",
        "Full stop",
        "Greek ano teleia",
        "Hebrew mark lower dot",
        "Hebrew point dagesh or mapiq",
        "Hebrew point holam haser for vav",
        "Hebrew point sin dot",
        "Hyphenation point",
        "Medium black circle",
        "Middle dot",
        "Nko combining nasalization mark",
        "Nko combining short rising tone",
        "One dot leader",
        "Syriac feminine dot",
        "Syriac hbasa-esasa dotted",
        "Syriac qushshaya",
        "Syriac rukkakha",
        #"Raised dot",
        )

    TWO_DOTS_HORIZONTAL = unicode_charset("Two Dots Horizontal",
        "Braille pattern dots-14",
        "Braille pattern dots-25",
        "Braille pattern dots-36",
        "Braille pattern dots-78",
        "Byzantine musical symbol dipli",
        "Byzantine musical symbol isakia telous ichimatos",
        "Combining diaeresis below",
        "Combining diaeresis",
        "Diaeresis",
        "Double prime",
        "Double low-9 quotation mark",
        "Hebrew point tsere",
        "Hebrew punctuation gershayim",
        "Left double quotation mark",
        "Nko combining double dot above",
        "Right double quotation mark",
        "Syriac dotted zlama angular",
        "Syriac dotted zlama horizontal",
        "Syriac horizontal colon",
        "Two dot leader",
        )

    TWO_DOTS_VERTICAL = unicode_charset("Two Dots Vertical",
        "Arabic semicolon",
        "Armenian full stop",
        "Braille pattern dots-13",
        "Braille pattern dots-17",
        "Braille pattern dots-27",
        "Braille pattern dots-46",
        "Braille pattern dots-48",
        "Braille pattern dots-58",
        "Colon",
        "Greek question mark",
        "Hebrew punctuation sof pasuq",
        "Modifier letter colon",
        "Modifier letter raised colon",
        "Modifier letter triangular colon",
        "Musical symbol repeat dots",
        "Ratio",
        "Reversed semicolon",
        "Semicolon",
        "Syriac pthaha dotted",
        "Syriac sublinear colon",
        "Syriac supralinear colon",
        "Two dot punctuation",
        )

    TWO_DOTS_DIAGONAL = unicode_charset("Two Dots Diagonal",
        "Braille pattern dots-15",
        "Braille pattern dots-15",
        "Braille pattern dots-15",
        "Braille pattern dots-15",
        "Braille pattern dots-16",
        "Braille pattern dots-18",
        "Braille pattern dots-24",
        "Braille pattern dots-26",
        "Braille pattern dots-28",
        "Braille pattern dots-34",
        "Braille pattern dots-35",
        "Braille pattern dots-38",
        "Braille pattern dots-47",
        "Braille pattern dots-57",
        "Braille pattern dots-67",
        "Syriac colon skewed left",
        "Syriac sublinear colon skewed right",
        # "Syriac supralinear colon skewed left ",
        )

    TWO_DOTS = TWO_DOTS_HORIZONTAL + TWO_DOTS_VERTICAL + TWO_DOTS_DIAGONAL

    MULTI_DOTS_VERTICAL = unicode_charset("Many Dots Vertical",
        "Vertical ellipsis",
        "Tifinagh letter tuareg yagh",
        "Braille pattern dots-458",
        # "Triple colon operator",
        "Braille pattern dots-137",
        "Braille pattern dots-127",
        "Braille pattern dots-468",
        "Tricolon",
        "Latin small letter i with dot below",
        "Braille pattern dots-237",
        "Ethiopic question mark",
        "Braille pattern dots-456",
        "Braille pattern dots-568",
        "Braille pattern dots-123",
        "Dotted fence",
        "Tifinagh letter tuareg yah",
        )

    MULTI_DOTS_HORIZONTAL = unicode_charset("Many Dots Horizontal",
        "Horizontal ellipsis",
        "Midline horizontal ellipsis",
        "Monogram for earth",
        "Box drawings light triple dash horizontal",
        "Combining three dots above",
        "Tifinagh letter tuareg yaq",
        "Byzantine musical symbol saximata",
        "Box drawings heavy triple dash horizontal",
        "Combining triple underdot",
        "Byzantine musical symbol tripli",
        "Box drawings light quadruple dash horizontal",
        "Combining four dots above",
        "Ocr customer account number",
        "Box drawings heavy quadruple dash horizontal",
        "Byzantine musical symbol tetrapli",
        "Triple prime",
        "Vai syllable di",
        )

    MULTI_DOTS_DIAGONAL = unicode_charset("Many Dots Diagonal",
        "Down right diagonal ellipsis",
        "Hebrew point qubuts",
        "Buginese pallawa",
        "Up right diagonal ellipsis",
        "Ocr amount of check",
        "Braille pattern dots-347",
        "Braille pattern dots-457",
        "Byzantine musical symbol dyo"
        )

    MULTI_DOTS_MISC = unicode_charset("Many Dots Miscellaneous",
        # "Drive slow sign",
        "Proportion",
        "Tifinagh letter tuareg yakh",
        "Braille pattern dots-1346",
        "Squared four dot punctuation",
        "Braille pattern dots-2578",
        "Braille pattern dots-1478",
        "Braille pattern dots-1467",
        "Braille pattern dots-1245",
        "Ethiopic full stop",
        "Tifinagh letter ayer yagh",
        "Braille pattern dots-1358",
        "Braille pattern dots-13456",
        "Braille pattern dots-23578",
        "Digram for earth",
        "Combining cyrillic ten millions sign",
        )

    MULTI_DOTS = MULTI_DOTS_HORIZONTAL + MULTI_DOTS_VERTICAL + MULTI_DOTS_DIAGONAL + MULTI_DOTS_MISC

    DOTS = ONE_DOT + TWO_DOTS + MULTI_DOTS

    DOT_CHARSET_S = [ONE_DOT, TWO_DOTS, DOTS]

    # Small custom charsets that make nice mosaics when combined.
    TRIANGLE_MOSAIC = unicode_charset("Triangle Mosaic",
            "Black lower left triangle",
            "Black lower right triangle",
            "Black upper left triangle",
            "Black upper right triangle",
            )

    BLOCK_MOSAIC = unicode_charset("Block Mosaic",
            "UPPER HALF BLOCK",
            "LOWER HALF BLOCK",
            "FULL BLOCK",
            "LEFT HALF BLOCK",
            "RIGHT HALF BLOCK",
            )

    VERTICAL_BLOCK_MOSAIC = unicode_charset("Vertical Block Mosaic",
            "UPPER HALF BLOCK",
            "LOWER HALF BLOCK",
            "FULL BLOCK",
            )

    HORIZONTAL_BLOCK_MOSAIC = unicode_charset("Horizontal Block Mosaic",
            "LEFT HALF BLOCK",
            "RIGHT HALF BLOCK",
            "FULL BLOCK",
            )

    TERMINAL_GRAPHIC_MOSAIC = unicode_charset("Terminal Graphic Mosaic",
            "QUADRANT LOWER LEFT",
            "QUADRANT LOWER RIGHT",
            "QUADRANT UPPER LEFT",
            "QUADRANT UPPER LEFT AND LOWER LEFT AND LOWER RIGHT",
            "QUADRANT UPPER LEFT AND LOWER RIGHT",
            "QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER LEFT",
            "QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER RIGHT",
            "QUADRANT UPPER RIGHT",
            "QUADRANT UPPER RIGHT AND LOWER LEFT",
            "QUADRANT UPPER RIGHT AND LOWER LEFT AND LOWER RIGHT",
            )

    SHADING_MOSAIC = unicode_charset("Shading Mosaic",
            "LIGHT SHADE",
            "MEDIUM SHADE",
            "DARK SHADE",
            "FULL BLOCK",
            )

    FILL_MOSAIC = unicode_charset("Fill Mosaic",
        "SQUARE WITH HORIZONTAL FILL", #▤
        "SQUARE WITH VERTICAL FILL", #▥
        "SQUARE WITH ORTHOGONAL CROSSHATCH FILL", #▦
        "SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL", #▧
        "SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL", #▨
        "SQUARE WITH DIAGONAL CROSSHATCH FILL", #▩
        )

    BOX_DRAWING_MOSAIC = unicode_charset("Box Drawing Light Mosaic",
            "BOX DRAWINGS LIGHT DOWN AND RIGHT",
            "BOX DRAWINGS LIGHT DOWN AND LEFT",
            "BOX DRAWINGS LIGHT UP AND LEFT",
            "BOX DRAWINGS LIGHT UP AND RIGHT",
            )

    BOX_DRAWING_HEAVY_MOSAIC = unicode_charset("Box Drawing Heavy Mosaic",
        "BOX DRAWINGS HEAVY HORIZONTAL", #━
        "BOX DRAWINGS HEAVY VERTICAL", #┃
        "BOX DRAWINGS HEAVY TRIPLE DASH HORIZONTAL", #┅
        "BOX DRAWINGS HEAVY TRIPLE DASH VERTICAL", #┇
        "BOX DRAWINGS HEAVY QUADRUPLE DASH HORIZONTAL", #┉
        "BOX DRAWINGS HEAVY QUADRUPLE DASH VERTICAL", #┋
        "BOX DRAWINGS HEAVY DOWN AND RIGHT", #┏
        "BOX DRAWINGS HEAVY DOWN AND LEFT", #┓
        "BOX DRAWINGS HEAVY UP AND RIGHT", #┗
        "BOX DRAWINGS HEAVY UP AND LEFT", #┛
        "BOX DRAWINGS HEAVY VERTICAL AND RIGHT", #┣
        "BOX DRAWINGS HEAVY VERTICAL AND LEFT", #┫
        "BOX DRAWINGS HEAVY DOWN AND HORIZONTAL", #┳
        "BOX DRAWINGS HEAVY UP AND HORIZONTAL", #┻
        "BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL", #╋
        "BOX DRAWINGS HEAVY DOUBLE DASH HORIZONTAL", #╍
        "BOX DRAWINGS HEAVY DOUBLE DASH VERTICAL", #╏
        "BOX DRAWINGS HEAVY LEFT", #╸
        "BOX DRAWINGS HEAVY UP", #╹
        "BOX DRAWINGS HEAVY RIGHT", #╺
        "BOX DRAWINGS HEAVY DOWN", #╻
        )

    BOX_DRAWING_ARC_MOSAIC = unicode_charset("Box Drawing Arc Mosaic",
            "BOX DRAWINGS LIGHT ARC DOWN AND RIGHT",
            "BOX DRAWINGS LIGHT ARC DOWN AND LEFT",
            "BOX DRAWINGS LIGHT ARC UP AND LEFT",
            "BOX DRAWINGS LIGHT ARC UP AND RIGHT",
            )

    CHARACTER_CELL_DIAGONAL_MOSAIC = unicode_charset("Character Cell Diagonal Mosaic",
            "BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT",
            "BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT",
            "BOX DRAWINGS LIGHT DIAGONAL CROSS",
            )

    PARTIALLY_FILLED_SQUARE_MOSAIC_DIAGONALS_ONLY = unicode_charset("Partially Filled Square Mosaic (Diagonals Only)",
        "SQUARE WITH UPPER RIGHT DIAGONAL HALF BLACK", #⬔
        "SQUARE WITH LOWER LEFT DIAGONAL HALF BLACK", #⬕
        "SQUARE WITH LOWER RIGHT DIAGONAL HALF BLACK", #◪
        "SQUARE WITH UPPER LEFT DIAGONAL HALF BLACK", #◩
        )

    PARTIALLY_FILLED_SQUARE_MOSAIC = unicode_charset(
        "Partially Filled Square Mosaic",
        "SQUARE WITH UPPER RIGHT DIAGONAL HALF BLACK", #⬔
        "SQUARE WITH LOWER LEFT DIAGONAL HALF BLACK", #⬕
        "SQUARE WITH LOWER RIGHT DIAGONAL HALF BLACK", #◪
        "SQUARE WITH UPPER LEFT DIAGONAL HALF BLACK", #◩
        "SQUARE WITH LEFT HALF BLACK", #◧
        "SQUARE WITH RIGHT HALF BLACK", #◨
        "SQUARE WITH TOP HALF BLACK", #⬒
        "SQUARE WITH BOTTOM HALF BLACK", #⬓
        )

    PARTIALLY_FILLED_CIRCLE_MOSAIC = unicode_charset("Partially Filled Circle Mosaic",
        "BLACK CIRCLE", #●
        "CIRCLE WITH LEFT HALF BLACK", #◐
        "CIRCLE WITH RIGHT HALF BLACK", #◑
        "CIRCLE WITH LOWER HALF BLACK", #◒
        "CIRCLE WITH UPPER HALF BLACK", #◓
        "CIRCLE WITH UPPER RIGHT QUADRANT BLACK", #◔
        "CIRCLE WITH ALL BUT UPPER LEFT QUADRANT BLACK", #◕
        )

    # These charsets can make a (potentially mirrorable) mosaic 
    # in conjunction with EM SPACE.
    TILABLE_CHARSET_S = [
        CUSTOM_ALPHABETS["Box Drawing Dots"],
        CUSTOM_ALPHABETS["Box Drawing Thick and Thin"],
        CUSTOM_ALPHABETS["Box Drawing Single and Double"],
        CUSTOM_ALPHABETS["Box Drawing Double"],
        CUSTOM_ALPHABETS["Block Drawing by Width"],
        CUSTOM_ALPHABETS["Block Drawing by Height"],
        "Yijing Hexagram Symbols",
        "Tai Xuan Jing Symbols",
        "Braille Patterns",
        "Emoji",
        BLOCK_MOSAIC,
        # CUSTOM_ALPHABETS["Box Drawing All"],
        # BOX_DRAWING_ARC_MOSAIC,
        PARTIALLY_FILLED_CIRCLE_MOSAIC,
        BOX_DRAWING_HEAVY_MOSAIC,
        BOX_DRAWING_MOSAIC,
        CHARACTER_CELL_DIAGONAL_MOSAIC,
        FILL_MOSAIC,
        HORIZONTAL_BLOCK_MOSAIC,
        PARTIALLY_FILLED_SQUARE_MOSAIC,
        SHADING_MOSAIC,
        TERMINAL_GRAPHIC_MOSAIC,
        VERTICAL_BLOCK_MOSAIC,
        RECTANGLES,
    ]

    MOSAIC_CHARSET_S = [
        CUSTOM_ALPHABETS["Completely Circled Alphabetics"],
        CUSTOM_ALPHABETS["Fullwidth Alphabetics"],
        CUSTOM_ALPHABETS["Double Circled Numerics"],
        CUSTOM_ALPHABETS["Filled Circled Numerics"],
        CUSTOM_ALPHABETS["Empty Circled Numerics"],
        CUSTOM_ALPHABETS["Dice"],
        CUSTOM_ALPHABETS["Box Drawing All"],
        CUSTOM_ALPHABETS["Box Drawing Dots"],
        CUSTOM_ALPHABETS["Box Drawing Thick and Thin"],
        CUSTOM_ALPHABETS["Box Drawing Single and Double"],
        CUSTOM_ALPHABETS["Box Drawing Double"],
        CUSTOM_ALPHABETS["Block Drawing by Width"],
        CUSTOM_ALPHABETS["Block Drawing by Height"],
        CUSTOM_ALPHABETS["Skin Tones"],
        RECTANGLES,
        BLOCK_MOSAIC,
        BOX_DRAWING_ARC_MOSAIC,
        BOX_DRAWING_HEAVY_MOSAIC,
        BOX_DRAWING_MOSAIC,
        CHARACTER_CELL_DIAGONAL_MOSAIC,
        FILL_MOSAIC,
        HORIZONTAL_BLOCK_MOSAIC,
        PARTIALLY_FILLED_CIRCLE_MOSAIC,
        PARTIALLY_FILLED_SQUARE_MOSAIC,
        SHADING_MOSAIC,
        TERMINAL_GRAPHIC_MOSAIC,
        VERTICAL_BLOCK_MOSAIC,
        TRIANGLES,
        ]

    EMOJI_S = [
        "Miscellaneous Symbols And Pictographs",
        "Transport and Map Symbols",
        "Emoticons",
        ]

    WHITESPACE = unicode_charset(
        "NO-BREAK SPACE",
        "EN QUAD",
        "EM QUAD",
        "EN SPACE",
        "EM SPACE",
        "THREE-PER-EM SPACE",
        "FOUR-PER-EM SPACE",
        "SIX-PER-EM SPACE",
        "FIGURE SPACE",
        "PUNCTUATION SPACE",
        "THIN SPACE",
        "HAIR SPACE",
        "NARROW NO-BREAK SPACE",
        "MEDIUM MATHEMATICAL SPACE",
        "IDEOGRAPHIC SPACE",
    )
