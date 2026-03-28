# coding=utf-8
"""Unicode glyphs that resemble other glyphs."""

__all__ = ["alternate_spelling"]

import random
import string

alternates = {
    "a" : u"",
    "b" : u"",
    "c" : u"ϲᒼᑦсϚⅽ꜀꜂ℂ℃⊏",
    "d" : u"",
    "e" : u"💶ᥱ",    
    "f" : u"ſʄ",
    "g" : u"",    
    "h" : u"ℌᑋ",
    "i" : u"",    
    "j" : u"",
    "k" : u"ⱪ",    
    "l" : u"",
    "m" : u"ϻ⩋ᨓოጦጠᶬ₥ෆ",
    "n" : u"⩏സﬨヘ",
    "o" : u"",    
    "p" : u"ᕵᑭᑭⲢ",
    "q" : u"",    
    "r" : u"╭┌ɼᒋᒥ꜒Γᖋ┍ᒋℾᒋɼґᣘ𝝘ⲅ𝈬꜓⦧",
    "s" : u"",    
    "t" : u"†Ϯϯ┼┽┿╀⍭┾╇+ⵜ╁╪╈╅╅╆╄⨨╂╃╉╊╋╉ߙ⁺ᚐႵ⍖Էէヒナヒモ",
    "u" : u"Цυսᥙɥᐡ",
    "v" : u"",
    "w" : u"ᐜ",    
    "x" : u"☒",
    "y" : u"ʮկ",    
    "z" : u"",

    "A" : u"⍍ᐃ",
    "B" : u"β3",
    "C" : u"ᑕϹСʗⅭⵎᥴⲤƇᑕ",    
    "D" : u"ᐅᑓᑔ",
    "E" : u"⪡ΕꗋΕƐЄᎬⴹЕĘɛℇᙓミ",
    "F" : u"ҒϜғƑߓ𝟋₣ᖴ╒𐌅℉",
    "G" : u"",    
    "H" : u"╫⩆",
    "I" : u"エェヱ",
    "J" : u"",
    "K" : u"ΚƘKК𐌊ҚкⱩⲔκᏦϏҜ𝝟₭ꗪ",    
    "L" : u"レ",
    "M" : u"ΜМϺ𐌑ⅯмⱮӍ𝝡ӎ",
    "N" : u"₪Иⵍи",
    "O" : u"🝕▣⌻⏣⧈0ロ",
    "P" : u"ꝒР♇ҏРΡᏢ⛿ᕈ𐌛Ᵽ𐌓ǷⲢ℗アァ",
    "Q" : u"",    
    "R" : u"𝈖ᎡƦɌⴽᖇ",
    "S" : u"⑀",    
    "T" : u"⊤┬ΤТ⟙ꔋ𝖳┰┯т𝍮⫪┮Ƭ🝨⥡┭Ţ⏉ᚁᎢ┳╥𝝩Ꞇィイフヮワᐪ",
    "U" : u"⋃⨆ᑌ∪ՍⵡŲ∐⌴ᓑԱ⊔𝈈பVリᑌ",
    "V" : u"ᐺ",
    "W" : u"",    
    "X" : u"⪥",
    "Y" : u"߂ЏЦ💴",
    "Z" : u"",
    "-" : u"ー",
}

multi_character_alternates = {
    "B" : ["]3", "|3"],
    "H" : ["|-|", "|=|"],
    "K" : ["]<", ")<", "|<"],
    "O" : ["()", "[]", "{}"],
    "U" : ["|_|"],
    "V" : ["\/"],
}

from olipy.alphabet import CUSTOM_ALPHABETS

alternate_letterforms = {}
for k, v in alternates.items():
    alternate_letterforms[k] = set(v)
for k, v in multi_character_alternates.items():
    alternate_letterforms[k].update(v)

full_alphabet_mapping = string.ascii_uppercase + string.ascii_lowercase
lowercase_alphabet_mapping = string.ascii_lowercase
def map_alphabet(alphabet, mapping=full_alphabet_mapping):
    for i, char in enumerate(alphabet):
        if not char.strip():
            continue
        map_to = mapping[i]
        alternate_letterforms[map_to].add(char)
    
# Incorporate some strings that map the alphabet onto alternate 'fonts'.
for alphabet_name in [
        "Completely Circled Alphabetics",
        "Fullwidth Alphabetics" ,
        "Bold Alphabetics" ,
        "Italic Alphabetics" ,
        "Bold Italic Alphabetics" ,
        "Script Alphabetics" ,
        "Script Bold Alphabetics" ,
        "Fraktur Alphabetics" ,
        "Doublestruck Alphabetics" ,
        "Fraktur Bold Alphabetics" ,
        "Sans Alphabetics" ,
        "Sans Bold Alphabetics" ,
        "Sans Italic Alphabetics" ,
        "Sans Bold Italic Alphabetics" ,
        "Monospace Alphabetics" ,
#        "Alphabetics with Umlaut" ,
]:
    alphabet = CUSTOM_ALPHABETS[alphabet_name]
    map_alphabet(alphabet)

full_alphabets = [
    u"ᴬᴮʿᴰᴱ ᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾ ᴿ ᵀᵁⱽᵂ   ₐᵇ ᵈᵉᶠᵍʰᶤʲᵏˡᵐᵑᵒᵖ ʳˢᵗᵤᵛʷˣʸᶻ",
    u"ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘ ʀꜱᴛᴜᴠᴡ ʏᴢₐ   ₑ  ₕᵢⱼₖₗₘₙₒₚ ᵣₛₜᵤᵥ ₓ  ",
]
for alphabet in full_alphabets:
    map_alphabet(alphabet)
    
lowercase_alphabets = [u"⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵"]
for alphabet in lowercase_alphabets:
    map_alphabet(alphabet, lowercase_alphabet_mapping)
    
# Finally, construct a case-insensitive version of alternate_letterforms.
alternate_letterforms_case_insensitive = dict()
for lower in string.ascii_lowercase:
    upper = lower.upper()
    combined = alternate_letterforms[lower].union(alternate_letterforms[upper])
    for destination in (lower, upper):
        alternate_letterforms_case_insensitive[destination] = combined

def alternate_spelling(string, case_sensitive=False):
    new_string = u""
    if case_sensitive:
        source = alternate_letterforms
    else:
        source = alternate_letterforms_case_insensitive
    for char in string:
        if char in source and source[char]:
            char = random.choice(list(source[char]))
        new_string += char
    return new_string
