
# 한글 점자
# 초성
han_cho_dict = {
    'ㄱ': '⠈',
    'ㄲ': '⠠⠈',
    'ㄴ': '⠉',
    'ㄷ': '⠊',
    'ㄸ': '⠠⠊',
    'ㄹ': '⠐',
    'ㅁ': '⠑',
    'ㅂ': '⠘',
    'ㅃ': '⠠⠘',
    'ㅅ': '⠠',
    'ㅆ': '⠠⠠',
    'ㅇ': '⠛',   # 사용되지 않음
    'ㅈ': '⠨',
    'ㅉ': '⠠⠨',
    'ㅊ': '⠰',
    'ㅋ': '⠋',
    'ㅌ': '⠓',
    'ㅍ': '⠙',
    'ㅎ': '⠚',
    '된소리': '⠠',
}
# 중성
han_jung_dict = {
    'ㅏ': '⠣',
    'ㅑ': '⠜',
    'ㅓ': '⠎',
    'ㅕ': '⠱',
    'ㅗ': '⠥',
    'ㅛ': '⠬',
    'ㅜ': '⠍',
    'ㅠ': '⠩',
    'ㅡ': '⠪',
    'ㅣ': '⠕',
    'ㅐ': '⠗',
    'ㅒ': '⠜⠗',
    'ㅔ': '⠝',
    'ㅖ': '⠌',
    'ㅘ': '⠧',
    'ㅙ': '⠧⠗',
    'ㅚ': '⠽',
    'ㅝ': '⠏',
    'ㅞ': '⠏⠗',
    'ㅟ': '⠍⠗',
    'ㅢ': '⠺',
}
# 종성
han_jong_dict = {
    'ㄱ': '⠁',
    'ㄲ': '⠁⠁',
    'ㄴ': '⠒',
    'ㄷ': '⠔',
    'ㄹ': '⠂',
    'ㅁ': '⠢',
    'ㅂ': '⠃',
    'ㅅ': '⠄',
    'ㅆ': '⠌',
    'ㅇ': '⠶',
    'ㅈ': '⠅',
    'ㅊ': '⠆',
    'ㅋ': '⠖',
    'ㅌ': '⠦',
    'ㅍ': '⠲',
    'ㅎ': '⠴',
    'ㄳ': '⠁⠄',
    'ㄵ': '⠒⠅',
    'ㄶ': '⠒⠴',
    'ㄺ': '⠂⠁',
    'ㄻ': '⠂⠢',
    'ㄼ': '⠂⠃',
    'ㄽ': '⠂⠄',
    'ㄾ': '⠂⠦',
    'ㄿ': '⠂⠲',
    'ㅀ': '⠂⠴',
    'ㅄ': '⠃⠄',
}
han_jong_double = ['ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ', 'ㄲ', 'ㅆ']
han_jong_separate = {
    'ㄳ': ['ㄱ', 'ㅅ'],
    'ㄵ': ['ㄴ', 'ㅈ'],
    'ㄶ': ['ㄴ', 'ㅎ'],
    'ㄺ': ['ㄹ', 'ㄱ'],
    'ㄻ': ['ㄹ', 'ㅁ'],
    'ㄼ': ['ㄹ', 'ㅂ'],
    'ㄽ': ['ㄹ', 'ㅅ'],
    'ㄾ': ['ㄹ', 'ㅌ'],
    'ㄿ': ['ㄹ', 'ㅍ'],
    'ㅀ': ['ㄹ', 'ㅎ'],
    'ㅄ': ['ㅂ', 'ㅅ'],
    'ㄲ': ['ㄱ', 'ㄱ'],
    'ㅆ': ['ㅅ', 'ㅅ'],
}
# 약자
abb_char_dict = {
    'ㄱ': '⠫',
    'ㄲ': '⠠⠫',
    'ㄴ': '⠉',
    'ㄷ': '⠊',
    'ㄸ': '⠠⠊',
    'ㅁ': '⠑',
    'ㅂ': '⠘',
    'ㅃ': '⠠⠘',
    'ㅅ': '⠇',
    'ㅆ': '⠠⠇',
    'ㅇ': '⠣',
    'ㅈ': '⠨',
    'ㅉ': '⠠⠨',
    'ㅋ': '⠋',
    'ㅌ': '⠓',
    'ㅍ': '⠙',
    'ㅎ': '⠚',
    '것': '⠸⠎',
    '껏': '⠠⠸⠎',
    '억': '⠹',
    '언': '⠾',
    '얼': '⠞',
    '연': '⠡',
    '열': '⠳',
    '영': '⠻',
    '옥': '⠭',
    '온': '⠷',
    '옹': '⠿',
    '운': '⠛',
    '울': '⠯',
    '은': '⠵',
    '을': '⠮',
    '인': '⠟',
}
# 약어
abb_word_dict = {
    '그래서': '⠁⠎',
    '그러나': '⠁⠉',
    '그러면': '⠁⠒',
    '그러므로': '⠁⠢',
    '그런데': '⠁⠝',
    '그리고': '⠁⠥',
    '그리하여': '⠁⠱',
}

# 영어 점자
eng_start = '⠴'     # 로마자 시작
eng_end = '⠲'       # 로마자 끝
upper_case = '⠠'    # 대문자
eng_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': ' '
}
# 숫자 점자
num_start = '⠼'     # 수표
num_dict = {
    '0': '⠚', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙',
    '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊',
    '+': '⠢', '-': '⠔', '×': '⠡', '÷': '⠌⠌', '=': '⠒⠒',
}
