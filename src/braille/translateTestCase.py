
"""
    점자 번역 TestCase
    '한글 점자 규정 해설서'에 예문으로 나와있는 문장, 단어
"""
from src.braille.translate import translate

## 테스트 케이스
translateTestCase = {
    ## 제1절 제2항
    "아이" : "⠣⠕",
    "우유": "⠍⠩",
    "중앙": "⠨⠍⠶⠣⠶",
    "발음": "⠘⠂⠪⠢",
    "아버지": "⠣⠘⠎⠨⠕",
    "야유": "⠜⠩",
    "어머니": "⠎⠑⠎⠉⠕",
    "여우": "⠱⠍",
    "용": "⠬⠶",
    "우거지": "⠍⠈⠎⠨⠕",
    ## 제1절 제3항
    "솥뚜껑": "⠠⠥⠦⠠⠊⠍⠠⠈⠎⠶",
    "소뼈": "⠠⠥⠠⠘⠱",
    "쓰기": "⠠⠠⠪⠈⠕",
    "찌개": "⠠⠨⠕⠈⠗",
    ## 제2절 제4항
    "국어": "⠈⠍⠁⠎",
    "롤러": "⠐⠥⠂⠐⠎",
    "법률": "⠘⠎⠃⠐⠩⠂",
    "버섯": "⠘⠎⠠⠎⠄",
    "젖다": "⠨⠎⠅⠊",
    "꽃": "⠠⠈⠥⠆",
    "난중일기": "⠉⠒⠨⠍⠶⠕⠂⠈⠕",
    "딛다": "⠊⠕⠔⠊",
    "멈추다": "⠑⠎⠢⠰⠍⠊",
    "포용": "⠙⠥⠬⠶",
    "북녘": "⠘⠍⠁⠉⠱⠖",
    "밥솥": "⠘⠃⠠⠥⠦",
    "앞자리": "⠣⠲⠨⠐⠕",
    "좋다": "⠨⠥⠴⠊",
    "일자 형태의 부엌!": "⠕⠂⠨⠀⠚⠻⠓⠗⠺⠀⠘⠍⠎⠖⠖",
    ## 제2절 제5항
    "낚시": "⠉⠁⠁⠠⠕",
    "있다": "⠕⠌⠊",
    "안팎": "⠣⠒⠙⠁⠁",
    "보았다": "⠘⠥⠣⠌⠊",
    "깎았다": "⠠⠫⠁⠁⠣⠌⠊",
    "엮었다": "⠱⠁⠁⠎⠌⠊",
    "무예": "⠑⠍⠤⠌",
    "이지예": "⠕⠨⠕⠤⠌",
    ## 제2절 제6항
    "삯": "⠇⠁⠄",
    "앉다": "⠣⠒⠅⠊",
    "않다": "⠣⠒⠴⠊",
    "읽다": "⠕⠂⠁⠊",
    "옮기다": "⠥⠂⠢⠈⠕⠊",
    "밟다": "⠘⠂⠃⠊",
    "외곬": "⠽⠈⠥⠂⠄",
    "핥다": "⠚⠂⠦⠊",
    "읊다": "⠮⠲⠊",
    "옳다": "⠥⠂⠴⠊",
    "없다": "⠎⠃⠄⠊",
    "품삯": "⠙⠍⠢⠇⠁⠄",
    "앉은 자리": "⠣⠒⠅⠵⠀⠨⠐⠕",
    "많이": "⠑⠒⠴⠕",
    "칡차": "⠰⠕⠂⠁⠰⠣",
    "옮김": "⠥⠂⠢⠈⠕⠢",
    "얇다": "⠜⠂⠃⠊",
    "옰": "⠥⠂⠄",
    "개미핥기": "⠈⠗⠑⠕⠚⠂⠦⠈⠕",
    "앒": "⠣⠂⠲",
    "싫증": "⠠⠕⠂⠴⠨⠪⠶",
    "책값": "⠰⠗⠁⠫⠃⠄",
    "몫": "⠑⠭⠄",
    "얽매이다": "⠞⠁⠑⠗⠕⠊",
    "읊조리다": "⠮⠲⠨⠥⠐⠕⠊",
    ## 제3절 제8항
    "새우": "⠠⠗⠍",
    "얘기": "⠜⠗⠈⠕",
    "게으름": "⠈⠝⠪⠐⠪⠢",
    "예약": "⠌⠜⠁",
    "관람": "⠈⠧⠒⠐⠣⠢",
    "쇄국": "⠠⠧⠗⠈⠍⠁",
    "쇠고기": "⠠⠽⠈⠥⠈⠕",
    "권리": "⠈⠏⠒⠐⠕",
    "스웨터": "⠠⠪⠏⠗⠓⠎",
    "취소": "⠰⠍⠗⠠⠥",
    "의식": "⠺⠠⠕⠁",
    "톈진 조약은 1884년 갑신정변 후 일본과 청이 맺은 조약이다.": "⠓⠌⠒⠨⠟⠀⠨⠥⠜⠁⠵⠀⠼⠁⠓⠓⠙⠀⠉⠡⠀⠫⠃⠠⠟⠨⠻⠘⠡⠀⠚⠍⠀⠕⠂⠘⠷⠈⠧⠀⠰⠻⠕⠀⠑⠗⠅⠵⠀⠨⠥⠜⠁⠕⠊⠲",
    ## 제4절 제9항
    "‘ㅆ’의 이름은 쌍시옷이다.": "⠠⠦⠿⠠⠠ ⠴⠄⠺⠀⠕⠐⠪⠢⠵⠀⠠⠇⠶⠠⠕⠥⠄⠕⠊⠲",
    "‘ㅆ’ 받침을 ‘ㅅ’ 받침 하나로 적는 것은 흔한 맞춤법 오류이다.": "⠠⠦⠿⠠⠠ ⠴⠄⠀⠘⠔⠰⠕⠢⠮⠀⠠⠦⠿⠠ ⠴⠄⠀⠘⠔⠰⠕⠢⠀⠚⠉⠐⠥⠀⠨⠹⠉⠵⠀⠸⠎⠵⠀⠚⠵⠚⠒⠀⠑⠅⠰⠍⠢⠘⠎⠃⠀⠥⠐⠩⠕⠊⠲",
    "‘ㅖ’는 한글 자모 ‘ㅕ’와 ‘ㅣ’를 어울러 쓴 글자이다.": "⠠⠦⠿⠌⠀⠴⠄⠉⠵⠀⠚⠒⠈⠮⠀⠨⠑⠥⠀⠠⠦⠿⠱⠀⠴⠄⠧⠀⠠⠦⠿⠕⠀⠴⠄⠐⠮⠀⠎⠯⠐⠎⠀⠠⠠⠵⠀⠈⠮⠨⠣⠕⠊⠲",
    "전통적인 ㄱ자 초가집": "⠨⠾⠓⠿⠨⠹⠟⠀⠿⠈⠀⠨⠀⠰⠥⠫⠨⠕⠃",
    "ㄱ의 구개음화": "⠿⠈⠀⠺⠀⠈⠍⠈⠗⠪⠢⠚⠧",
    ## 제5절 제10항
    "아예": "⠣⠤⠌",
    "도예": "⠊⠥⠤⠌",
    "뭐예요": "⠑⠏⠤⠌⠬",
    "서예": "⠠⠎⠤⠌",
    "추사 김정희는 유명한 서예가입니다.": "⠰⠍⠇⠀⠈⠕⠢⠨⠻⠚⠺⠉⠵⠀⠩⠑⠻⠚⠒⠀⠠⠎⠤⠌⠫⠕⠃⠉⠕⠊⠲",
    "오예": "⠥⠤⠌",
    "이예은": "⠕⠤⠌⠵",
    "그는 정상이 참작되어 기소 유예로 풀려났다.": "⠈⠪⠉⠵⠀⠨⠻⠇⠶⠕⠀⠰⠣⠢⠨⠁⠊⠽⠎⠀⠈⠕⠠⠥⠀⠩⠤⠌⠐⠥⠀⠙⠯⠐⠱⠉⠌⠊⠲",
    "노예로 팔리다.": "⠉⠥⠤⠌⠐⠥⠀⠙⠂⠐⠕⠊⠲",
    "예예, 잘 알겠습니다.": "⠌⠤⠌⠐⠀⠨⠂⠀⠣⠂⠈⠝⠌⠠⠪⠃⠉⠕⠊⠲",
    "옜다, 너 요걸로 먹고 싶은 것 사 먹어라.": "⠌⠌⠊⠐⠀⠉⠎⠀⠬⠈⠞⠐⠥⠀⠑⠹⠈⠥⠀⠠⠕⠲⠵⠀⠸⠎⠀⠇⠀⠑⠹⠎⠐⠣⠲",
    "그는 문학에 조예가 깊다.": "⠈⠪⠉⠵⠀⠑⠛⠚⠁⠝⠀⠨⠥⠤⠌⠫⠀⠈⠕⠲⠊⠲",
    "예술 분야 중에도 특히 음악에 조예가 깊다.": "⠌⠠⠯⠀⠘⠛⠜⠀⠨⠍⠶⠝⠊⠥⠀⠓⠪⠁⠚⠕⠀⠪⠢⠣⠁⠝⠀⠨⠥⠤⠌⠫⠀⠈⠕⠲⠊⠲",
    ## 제5절 제11항
    "야애": "⠜⠤⠗",
    "소화액": "⠠⠥⠚⠧⠤⠗⠁",
    "구애": "⠈⠍⠤⠗",
    "침, 쓸개즙 등의 소화액은 소화 효소를 가지고 있다.": "⠰⠕⠢⠐⠀⠠⠠⠮⠈⠗⠨⠪⠃⠀⠊⠪⠶⠺⠀⠠⠥⠚⠧⠤⠗⠁⠵⠀⠠⠥⠚⠧⠀⠚⠬⠠⠥⠐⠮⠀⠫⠨⠕⠈⠥⠀⠕⠌⠊⠲",
    "《야앵》은 1936년에 발표된 김유정의 단편 소설이다.": "⠰⠦⠜⠤⠗⠶⠴⠆⠵⠀⠼⠁⠊⠉⠋⠀⠉⠡⠝⠀⠘⠂⠙⠬⠊⠽⠒⠀⠈⠕⠢⠩⠨⠻⠺⠀⠊⠒⠙⠡⠀⠠⠥⠠⠞⠕⠊⠲",
    "세금 부과액이 너무 과하다.": "⠠⠝⠈⠪⠢⠀⠘⠍⠈⠧⠤⠗⠁⠕⠀⠉⠎⠑⠍⠀⠈⠧⠚⠊⠲",
    "나무의 수액이 흘러나왔다.": "⠉⠑⠍⠺⠀⠠⠍⠤⠗⠁⠕⠀⠚⠮⠐⠎⠉⠣⠧⠌⠊⠲",
    "가나스기 겐지 외무성 아시아대양주국장은 주일 중국대사관 궈앤 공사에게 항의했다.": "⠫⠉⠠⠪⠈⠕⠀⠈⠝⠒⠨⠕⠀⠽⠑⠍⠠⠻⠀⠣⠠⠕⠣⠊⠗⠜⠶⠨⠍⠈⠍⠁⠨⠶⠵⠀⠨⠍⠕⠂⠀⠨⠍⠶⠈⠍⠁⠊⠗⠇⠈⠧⠒⠀⠈⠏⠤⠗⠒⠀⠈⠿⠇⠝⠈⠝⠀⠚⠶⠺⠚⠗⠌⠊⠲",
    "무엇보다 조기 진단과 적절한 수액 공급이 필수적이다.": "⠑⠍⠎⠄⠘⠥⠊⠀⠨⠥⠈⠕⠀⠨⠟⠊⠒⠈⠧⠀⠨⠹⠨⠞⠚⠒⠀⠠⠍⠤⠗⠁⠀⠈⠿⠈⠪⠃⠕⠀⠙⠕⠂⠠⠍⠨⠹⠕⠊⠲",
    "액면 초과액이란 액면 주식을 액면 초과하여 발행한 경우의 초과액이다.": "⠗⠁⠑⠡⠀⠰⠥⠈⠧⠤⠗⠁⠕⠐⠣⠒⠀⠗⠁⠑⠡⠀⠨⠍⠠⠕⠁⠮⠀⠗⠁⠑⠡⠀⠰⠥⠈⠧⠚⠣⠱⠀⠘⠂⠚⠗⠶⠚⠒⠀⠈⠻⠍⠺⠀⠰⠥⠈⠧⠤⠗⠁⠕⠊⠲",
    ## 제6절 제12항
    "가자": "⠫⠨",
    "바다": "⠘⠊",
    "자동차": "⠨⠊⠿⠰⠣",
    "가위": "⠫⠍⠗",
    "사격": "⠇⠈⠱⠁",
    "나들이": "⠉⠊⠮⠕",
    "다르다": "⠊⠐⠪⠊",
    "마당": "⠑⠊⠶",
    "바나나": "⠘⠉⠉",
    "자격증": "⠨⠈⠱⠁⠨⠪⠶",
    "카네기": "⠋⠉⠝⠈⠕",
    "균형타": "⠈⠩⠒⠚⠻⠓",
    "과격파": "⠈⠧⠈⠱⠁⠙",
    "하도급": "⠚⠊⠥⠈⠪⠃",
    "다음": "⠊⠣⠪⠢",
    "마음": "⠑⠣⠪⠢",
    "하얀": "⠚⠣⠜⠒",
    "카카오": "⠋⠋⠣⠥",
    "타이어": "⠓⠣⠕⠎",
    "파이프": "⠙⠣⠕⠙⠪",
    "콜레라": "⠋⠥⠂⠐⠝⠐⠣",
    "기차": "⠈⠕⠰⠣",
    "얼룩소": "⠞⠐⠍⠁⠠⠥",
    "열거": "⠳⠈⠎",
    "은빛": "⠵⠘⠕⠆",
    "가을": "⠫⠮",
    "언급": "⠾⠈⠪⠃",
    "촬영": "⠰⠧⠂⠻",
    "온기": "⠷⠈⠕",
    "서울": "⠠⠎⠯",
    "크레인": "⠋⠪⠐⠝⠟",
    "1점은 첫째 언니": "⠼⠁⠨⠎⠢⠵⠀⠰⠎⠄⠠⠨⠗⠀⠾⠉⠕",
    "4점은 삼한사온": "⠼⠙⠨⠎⠢⠵⠀⠇⠢⠚⠒⠇⠷",
    "6점은 6인": "⠼⠋⠨⠎⠢⠵⠀⠼⠋⠟",
    "기억": "⠈⠕⠹",
    "지옥": "⠨⠕⠭",
    "옹달샘": "⠿⠊⠂⠠⠗⠢",
    "혜운": "⠚⠌⠛",
    "기역처럼 생긴 억": "⠈⠕⠱⠁⠰⠎⠐⠎⠢⠀⠠⠗⠶⠈⠟⠀⠹",
    "구슬처럼 속이 빈 옥": "⠈⠍⠠⠮⠰⠎⠐⠎⠢⠀⠠⠭⠕⠀⠘⠟⠀⠭",
    "옹골차게 꽉 찬 옹": "⠿⠈⠥⠂⠰⠣⠈⠝⠀⠠⠈⠧⠁⠀⠰⠣⠒⠀⠿",
    "구름처럼 둥둥 떠 있는 운": "⠈⠍⠐⠪⠢⠰⠎⠐⠎⠢⠀⠊⠍⠶⠊⠍⠶⠀⠠⠊⠎⠀⠕⠌⠉⠵⠀⠛",
    "인연": "⠟⠡",
    "연예인": "⠡⠌⠟",
    "그것": "⠈⠪⠸⠎",
    "아무것": "⠣⠑⠍⠸⠎",
    ## 제6절 제13항
    "강산": "⠫⠶⠇⠒",
    "난방": "⠉⠒⠘⠶",
    "달밤": "⠊⠂⠘⠢",
    "감칠맛": "⠫⠢⠰⠕⠂⠑⠄",
    "낙엽": "⠉⠁⠱⠃",
    "망망대해": "⠑⠶⠑⠶⠊⠗⠚⠗",
    "칼국수": "⠋⠂⠈⠍⠁⠠⠍",
    ## 제6절 제14항
    "까치": "⠠⠫⠰⠕",
    "깡충깡충": "⠠⠫⠶⠰⠍⠶⠠⠫⠶⠰⠍⠶",
    "쌍둥이": "⠠⠇⠶⠊⠍⠶⠕",
    "쌍쌍이": "⠠⠇⠶⠠⠇⠶⠕",
    "한껏": "⠚⠒⠠⠸⠎",
    "힘껏": "⠚⠕⠢⠠⠸⠎",
    "불을 껐다.": "⠘⠯⠮⠀⠠⠈⠎⠌⠊⠲",
    "까마귀": "⠠⠫⠑⠈⠍⠗",
    "쌀통": "⠠⠇⠂⠓⠿",
    "정성껏": "⠨⠻⠠⠻⠠⠸⠎",
    "우리네야 어찌 알겄소.": "⠍⠐⠕⠉⠝⠜⠀⠎⠠⠨⠕⠀⠣⠂⠈⠎⠌⠠⠥⠲",
    "형광등 스위치를 껐다 켰다.": "⠚⠻⠈⠧⠶⠊⠪⠶⠀⠠⠪⠍⠗⠰⠕⠐⠮⠀⠠⠈⠎⠌⠊⠀⠋⠱⠌⠊⠲",
    ## 제6절 제15항
    "꺾다": "⠠⠈⠹⠁⠊",
    "넋": "⠉⠹⠄",
    "덕망": "⠊⠹⠑⠶",
    "건전": "⠈⠾⠨⠾",
    "얹다": "⠾⠅⠊",
    "천하": "⠰⠾⠚",
    "넓다": "⠉⠞⠃⠊",
    "얽다": "⠞⠁⠊",
    "젊다": "⠨⠞⠢⠊",
    "견학": "⠈⠡⠚⠁",
    "변화": "⠘⠡⠚⠧",
    "현황": "⠚⠡⠚⠧⠶",
    "별": "⠘⠳",
    "엷다": "⠳⠃⠊",
    "혈기": "⠚⠳⠈⠕",
    "경성": "⠈⠻⠠⠻",
    "병원": "⠘⠻⠏⠒",
    "평화": "⠙⠻⠚⠧",
    "곡식": "⠈⠭⠠⠕⠁",
    "볶다": "⠘⠭⠁⠊",
    "폭포": "⠙⠭⠙⠥",
    "논": "⠉⠷",
    "돈": "⠊⠷",
    "손": "⠠⠷",
    "공사": "⠈⠿⠇",
    "송이": "⠠⠿⠕",
    "홍삼": "⠚⠿⠇⠢",
    "군대": "⠈⠛⠊⠗",
    "눈물": "⠉⠛⠑⠯",
    "문화": "⠑⠛⠚⠧",
    "굵다": "⠈⠯⠁⠊",
    "굶다": "⠈⠯⠢⠊",
    "훑다": "⠚⠯⠦⠊",
    "끊다": "⠠⠈⠵⠴⠊",
    "큰언니": "⠋⠵⠾⠉⠕",
    "튼튼한": "⠓⠵⠓⠵⠚⠒",
    "긁다": "⠈⠮⠁⠊",
    "늙다": "⠉⠮⠁⠊",
    "민족": "⠑⠟⠨⠭",
    "신라": "⠠⠟⠐⠣",
    "진실": "⠨⠟⠠⠕⠂",
    "고즈넉": "⠈⠥⠨⠪⠉⠹",
    "넌더리": "⠉⠾⠊⠎⠐⠕",
    "널뛰기": "⠉⠞⠠⠊⠍⠗⠈⠕",
    "면발": "⠑⠡⠘⠂",
    "별검": "⠘⠳⠈⠎⠢",
    "용병": "⠬⠶⠘⠻",
    "녹용": "⠉⠭⠬⠶",
    "논두렁": "⠉⠷⠊⠍⠐⠎⠶",
    "농구": "⠉⠿⠈⠍",
    "모눈": "⠑⠥⠉⠛",
    "둘째": "⠊⠯⠠⠨⠗",
    "토큰": "⠓⠥⠋⠵",
    "그늘": "⠈⠪⠉⠮",
    "진격": "⠨⠟⠈⠱⠁",
    "넓지도 않은 선반에 얹혔을 성냥갑은 얼른 찾아지지 않았다.": "⠉⠞⠃⠨⠕⠊⠥⠀⠣⠒⠴⠵⠀⠠⠾⠘⠒⠝⠀⠾⠅⠚⠱⠌⠮⠀⠠⠻⠉⠜⠶⠫⠃⠵⠀⠞⠐⠵⠀⠰⠣⠅⠣⠨⠕⠨⠕⠀⠣⠒⠴⠣⠌⠊⠲",
    "그는 뒤섞인 손님들의 신발을 가지런히 정리하였다.": "⠈⠪⠉⠵⠀⠊⠍⠗⠠⠹⠁⠟⠀⠠⠷⠉⠕⠢⠊⠮⠺⠀⠠⠟⠘⠂⠮⠀⠫⠨⠕⠐⠾⠚⠕⠀⠨⠻⠐⠕⠚⠣⠱⠌⠊⠲",
    ## 제6절 제16항
    "성가": "⠠⠻⠫",
    "말썽": "⠑⠂⠠⠠⠻",
    "정성": "⠨⠻⠠⠻",
    "어정쩡": "⠎⠨⠻⠠⠨⠻",
    "청년": "⠰⠻⠉⠡",
    "정성을 들였다고 마음을 놓지 마라.": "⠨⠻⠠⠻⠮⠀⠊⠮⠱⠌⠊⠈⠥⠀⠑⠣⠪⠢⠮⠀⠉⠥⠴⠨⠕⠀⠑⠐⠣⠲",
    "어머니는 눈물을 글썽거리셨다.": "⠎⠑⠎⠉⠕⠉⠵⠀⠉⠛⠑⠯⠮⠀⠈⠮⠠⠠⠻⠈⠎⠐⠕⠠⠱⠌⠊⠲",
    "멀쩡하던 하늘에 갑자기 먹구름이 몰려왔다.": "⠑⠞⠠⠨⠻⠚⠊⠾⠀⠚⠉⠮⠝⠀⠫⠃⠨⠈⠕⠀⠑⠹⠈⠍⠐⠪⠢⠕⠀⠑⠥⠂⠐⠱⠧⠌⠊⠲",
    "그는 청바지를 즐겨 입는다.": "⠈⠪⠉⠵⠀⠰⠻⠘⠨⠕⠐⠮⠀⠨⠮⠈⠱⠀⠕⠃⠉⠵⠊⠲",
    "개가 컹컹 짖다.": "⠈⠗⠫⠀⠋⠎⠶⠋⠎⠶⠀⠨⠕⠅⠊⠲",
    "덩어리": "⠊⠎⠶⠎⠐⠕",
    "텅 빈 들녘": "⠓⠎⠶⠀⠘⠟⠀⠊⠮⠉⠱⠖",
    ## 제6절 제17항
    "나이": "⠉⠣⠕",
    "마을": "⠑⠣⠮",
    "바위": "⠘⠣⠍⠗",
    "자아": "⠨⠣⠣",
    "땅을 팠다.": "⠠⠊⠶⠮⠀⠙⠣⠌⠊⠲",
    "철수는 여름 방학을 맞아 바위섬으로 놀러 갔다.": "⠰⠞⠠⠍⠉⠵⠀⠱⠐⠪⠢⠀⠘⠶⠚⠁⠮⠀⠑⠅⠣⠀⠘⠣⠍⠗⠠⠎⠢⠪⠐⠥⠀⠉⠥⠂⠐⠎⠀⠫⠌⠊⠲",
    "어머니는 길에 나오셔서 아들을 기다리셨다.": "⠎⠑⠎⠉⠕⠉⠵⠀⠈⠕⠂⠝⠀⠉⠣⠥⠠⠱⠠⠎⠀⠣⠊⠮⠮⠀⠈⠕⠊⠐⠕⠠⠱⠌⠊⠲",
    "파인애플을 먹었다.": "⠙⠣⠟⠗⠙⠮⠮⠀⠑⠹⠎⠌⠊⠲",
    "때는 바야흐로 만물이 소생하는 봄이다.": "⠠⠊⠗⠉⠵⠀⠘⠣⠜⠚⠪⠐⠥⠀⠑⠒⠑⠯⠕⠀⠠⠥⠠⠗⠶⠚⠉⠵⠀⠘⠥⠢⠕⠊⠲",
    "그는 지금 자아도취 상태에서 헤어나지 못하고 있다.": "⠈⠪⠉⠵⠀⠨⠕⠈⠪⠢⠀⠨⠣⠣⠊⠥⠰⠍⠗⠀⠇⠶⠓⠗⠝⠠⠎⠀⠚⠝⠎⠉⠨⠕⠀⠑⠥⠄⠚⠈⠥⠀⠕⠌⠊⠲",
    "계산은 카운터에서 하시기 바랍니다.": "⠈⠌⠇⠒⠵⠀⠋⠣⠛⠓⠎⠝⠠⠎⠀⠚⠠⠕⠈⠕⠀⠘⠐⠣⠃⠉⠕⠊⠲",
    "글 가운데에서 대화문임을 나타낼 때 큰따옴표를 쓴다.": "⠈⠮⠀⠫⠛⠊⠝⠝⠠⠎⠀⠊⠗⠚⠧⠑⠛⠕⠢⠮⠀⠉⠓⠉⠗⠂⠀⠠⠊⠗⠀⠋⠵⠠⠊⠣⠥⠢⠙⠬⠐⠮⠀⠠⠠⠵⠊⠲",
    "아빠, 빠이빠이.": "⠣⠠⠘⠐⠀⠠⠘⠣⠕⠠⠘⠣⠕⠲",
    "태국에 짜오프라야강이 있다.": "⠓⠗⠈⠍⠁⠝⠀⠠⠨⠣⠥⠙⠪⠐⠣⠜⠫⠶⠕⠀⠕⠌⠊⠲",
    "마음이 애달팠다.": "⠑⠣⠪⠢⠕⠀⠗⠊⠂⠙⠣⠌⠊⠲",
    "아녜스는 그리스어로 ‘순결’ 또는 ‘양’을 뜻한다.": "⠣⠉⠌⠠⠪⠉⠵⠀⠈⠪⠐⠕⠠⠪⠎⠐⠥⠀⠠⠦⠠⠛⠈⠳⠴⠄⠀⠠⠊⠥⠉⠵⠀⠠⠦⠜⠶⠴⠄⠮⠀⠠⠊⠪⠄⠚⠒⠊⠲",
    "중국 국민당 총재인 장개석의 중국식 발음은 장제스이나 장졔스로 표기하는 경우도 있다.": "⠨⠍⠶⠈⠍⠁⠀⠈⠍⠁⠑⠟⠊⠶⠀⠰⠿⠨⠗⠟⠀⠨⠶⠈⠗⠠⠹⠺⠀⠨⠍⠶⠈⠍⠁⠠⠕⠁⠀⠘⠂⠪⠢⠵⠀⠨⠶⠨⠝⠠⠪⠕⠉⠀⠨⠶⠨⠌⠠⠪⠐⠥⠀⠙⠬⠈⠕⠚⠉⠵⠀⠈⠻⠍⠊⠥⠀⠕⠌⠊⠲",
    "만약 당신이 불쾌한 상황에 처해 있다면 새로운 해석을 가미하여 빠져나올 수 있다.": "⠑⠒⠜⠁⠀⠊⠶⠠⠟⠕⠀⠘⠯⠋⠧⠗⠚⠒⠀⠇⠶⠚⠧⠶⠝⠀⠰⠎⠚⠗⠀⠕⠌⠊⠑⠡⠀⠠⠗⠐⠥⠛⠀⠚⠗⠠⠹⠮⠀⠫⠑⠕⠚⠣⠱⠀⠠⠘⠨⠱⠉⠣⠥⠂⠀⠠⠍⠀⠕⠌⠊⠲",
    "다예": "⠊⠤⠌",
    "나예림": "⠉⠤⠌⠐⠕⠢",
    ## 제6절 제18항
    "그래서인지": "⠁⠎⠟⠨⠕",
    "그러면서": "⠁⠒⠠⠎",
    "그런데도": "⠁⠝⠊⠥",
    "그리하여도": "⠁⠱⠊⠥",
    "쭈그리고": "⠠⠨⠍⠈⠪⠐⠕⠈⠥",
    "우그리고": "⠍⠈⠪⠐⠕⠈⠥",
    "오그리고": "⠥⠈⠪⠐⠕⠈⠥",
    "찡그리고": "⠠⠨⠕⠶⠈⠪⠐⠕⠈⠥",
    "그림을 그리고 있다.": "⠈⠪⠐⠕⠢⠮⠀⠁⠥⠀⠕⠌⠊⠲",
    "학생이 그래서 되겠느냐?": "⠚⠁⠠⠗⠶⠕⠀⠁⠎⠀⠊⠽⠈⠝⠌⠉⠪⠉⠜⠦",
    "나는 그림을 그리고 있었다.": "⠉⠉⠵⠀⠈⠪⠐⠕⠢⠮⠀⠁⠥⠀⠕⠌⠎⠌⠊⠲",
    "그러나저러나 이 일은 어차피 실패할 것이다.": "⠁⠉⠨⠎⠐⠎⠉⠀⠕⠀⠕⠂⠵⠀⠎⠰⠣⠙⠕⠀⠠⠕⠂⠙⠗⠚⠂⠀⠸⠎⠕⠊⠲",
    "동생은 그림을 그리고는 바로 잤다.": "⠊⠿⠠⠗⠶⠵⠀⠈⠪⠐⠕⠢⠮⠀⠁⠥⠉⠵⠀⠘⠐⠥⠀⠨⠌⠊⠲",
    "그런데도 아직 아무 연락이 없다.": "⠁⠝⠊⠥⠀⠣⠨⠕⠁⠀⠣⠑⠍⠀⠡⠐⠣⠁⠕⠀⠎⠃⠄⠊⠲",
    "다리를 쭈그리고 있었더니 저리다.": "⠊⠐⠕⠐⠮⠀⠠⠨⠍⠈⠪⠐⠕⠈⠥⠀⠕⠌⠎⠌⠊⠎⠉⠕⠀⠨⠎⠐⠕⠊⠲",
    "다리는 오그리고, 얼굴은 찡그리고 앉아 있는 못난이 인형": "⠊⠐⠕⠉⠵⠀⠥⠈⠪⠐⠕⠈⠥⠐⠀⠞⠈⠯⠵⠀⠠⠨⠕⠶⠈⠪⠐⠕⠈⠥⠀⠣⠒⠅⠣⠀⠕⠌⠉⠵⠀⠑⠥⠄⠉⠒⠕⠀⠟⠚⠻",
    "그는 뜨거운 햇볕에 얼굴을 찡그리고 손수건으로 이마의 땀을 닦았다.": "⠈⠪⠉⠵⠀⠠⠊⠪⠈⠎⠛⠀⠚⠗⠄⠘⠱⠦⠝⠀⠞⠈⠯⠮⠀⠠⠨⠕⠶⠈⠪⠐⠕⠈⠥⠀⠠⠷⠠⠍⠈⠾⠪⠐⠥⠀⠕⠑⠣⠺⠀⠠⠊⠢⠮⠀⠊⠁⠁⠣⠌⠊⠲",
    ## 제11절 제37항    # 숫자 부분
    "500": "⠼⠑⠚⠚",
    "123 4567": "⠼⠁⠃⠉⠀⠼⠙⠑⠋⠛",
    "1가": "⠼⠁⠫",
    "2권": "⠼⠃⠈⠏⠒",
    "3반": "⠼⠉⠘⠒",
    "4선": "⠼⠙⠠⠾",
    "5월": "⠼⠑⠏⠂",
    "6일": "⠼⠋⠕⠂",
    "7자루": "⠼⠛⠨⠐⠍",
    "8꾸러미": "⠼⠓⠠⠈⠍⠐⠎⠑⠕",
    # "1평은 3.3m²이다.": "",   # 특수문자, 영어 반영 후 추가 예정
    "1년": "⠼⠁⠀⠉⠡",
    "2도": "⠼⠃⠀⠊⠥",
    "3명": "⠼⠉⠀⠑⠻",
    "4칸": "⠼⠙⠀⠋⠒",
    "5톤": "⠼⠑⠀⠓⠷",
    "6평": "⠼⠋⠀⠙⠻",
    "7항": "⠼⠛⠀⠚⠶",
    "5운6기": "⠼⠑⠀⠛⠼⠋⠈⠕",
    # "79㎡형": "",   # 특수문자, 영어 반영 후 추가 예정
    "연필 8자루": "⠡⠙⠕⠂⠀⠼⠓⠨⠐⠍",
    "지우개 1개": "⠨⠕⠍⠈⠗⠀⠼⠁⠈⠗",
    "과자 1봉지": "⠈⠧⠨⠀⠼⠁⠘⠿⠨⠕",
    "점수 100점": "⠨⠎⠢⠠⠍⠀⠼⠁⠚⠚⠨⠎⠢",
    "고등어 2손": "⠈⠥⠊⠪⠶⠎⠀⠼⠃⠠⠷",
    "10 센티미터": "⠼⠁⠚⠀⠠⠝⠒⠓⠕⠑⠕⠓⠎",
    "8시 30분": "⠼⠓⠠⠕⠀⠼⠉⠚⠘⠛",
    "12월 25일": "⠼⠁⠃⠏⠂⠀⠼⠃⠑⠕⠂",
    "6학년": "⠼⠋⠀⠚⠁⠉⠡",
    "종이 2톤": "⠨⠿⠕⠀⠼⠃⠀⠓⠷",
    "1년 365일": "⠼⠁⠀⠉⠡⠀⠼⠉⠋⠑⠕⠂",
    "운동화 3켤레": "⠛⠊⠿⠚⠧⠀⠼⠉⠀⠋⠳⠐⠝",
    "360도": "⠼⠉⠋⠚⠀⠊⠥",
    "3면": "⠼⠉⠀⠑⠡",
    "3·1운동": "⠼⠉⠐⠆⠁⠀⠛⠊⠿", # 특수문자 반영 후 추가 예정
    "대한민국 임시 정부 수립일은 1919년 4월 13일이다.": "⠊⠗⠚⠒⠑⠟⠈⠍⠁⠀⠕⠢⠠⠕⠀⠨⠻⠘⠍⠀⠠⠍⠐⠕⠃⠕⠂⠵⠀⠼⠁⠊⠁⠊⠀⠉⠡⠀⠼⠙⠏⠂⠀⠼⠁⠉⠕⠂⠕⠊⠲",   # 특수문자 반영 후 추가 예정
    # "화상을 입은 면적이 100㎠나 되었다.": "⠼⠁⠃⠏⠂⠀⠼⠃⠑⠕⠂", # 특수문자, 영어 반영 후 추가 예정
    "1,234,567": "⠼⠁⠂⠃⠉⠙⠂⠑⠋⠛",
    "당첨금: 10,000,000,000원": "⠊⠶⠰⠎⠢⠈⠪⠢⠐⠂⠀⠼⠁⠚⠂⠚⠚⠚⠂⠚⠚⠚⠂⠚⠚⠚⠏⠒",
    "3년": "⠼⠉⠀⠉⠡",
    ## 제12절 제44항    # 특수 문자 부분
    "젊은이는 나라의 기둥이다.": "⠨⠞⠢⠵⠕⠉⠵⠀⠉⠐⠣⠺⠀⠈⠕⠊⠍⠶⠕⠊⠲",
    "집으로 돌아갑시다.": "⠨⠕⠃⠪⠐⠥⠀⠊⠥⠂⠣⠫⠃⠠⠕⠊⠲",
    "그는 “지금 바로 떠나자.”라고 말하며 서둘러 짐을 챙겼다.": "⠈⠪⠉⠵⠀⠦⠨⠕⠈⠪⠢⠀⠘⠐⠥⠀⠠⠊⠎⠉⠨⠲⠴⠐⠣⠈⠥⠀⠑⠂⠚⠑⠱⠀⠠⠎⠊⠯⠐⠎⠀⠨⠕⠢⠮⠀⠰⠗⠶⠈⠱⠌⠊⠲",
    "그는 “지금 바로 떠나자”라고 말하며 서둘러 짐을 챙겼다.": "⠈⠪⠉⠵⠀⠦⠨⠕⠈⠪⠢⠀⠘⠐⠥⠀⠠⠊⠎⠉⠨⠴⠐⠣⠈⠥⠀⠑⠂⠚⠑⠱⠀⠠⠎⠊⠯⠐⠎⠀⠨⠕⠢⠮⠀⠰⠗⠶⠈⠱⠌⠊⠲",
    "어제 오전에 보고서를 제출함.": "⠎⠨⠝⠀⠥⠨⠾⠝⠀⠘⠥⠈⠥⠠⠎⠐⠮⠀⠨⠝⠰⠯⠚⠢⠲",
    "내일 오전까지 보고서를 제출하기": "⠉⠗⠕⠂⠀⠥⠨⠾⠠⠫⠨⠕⠀⠘⠥⠈⠥⠠⠎⠐⠮⠀⠨⠝⠰⠯⠚⠈⠕",
    "3.14": "⠼⠉⠲⠁⠙",
    # "단원 13.a": "⠊⠒⠏⠒⠀⠼⠁⠉⠲⠴⠁⠲", # 영어 반영 후 추가 예정
    "이름이 뭐지?": "⠕⠐⠪⠢⠕⠀⠑⠏⠨⠕⠦",
    "진실하고 따뜻한 우정을 바라는가?": "⠨⠟⠠⠕⠂⠚⠈⠥⠀⠠⠊⠠⠊⠪⠄⠚⠒⠀⠍⠨⠻⠮⠀⠘⠐⠣⠉⠵⠫⠦",
    "“이 사람을 통해 어떤 이익을 얻을 수 있는가?”를 물어서는 안 된다.": "⠦⠕⠀⠇⠐⠣⠢⠮⠀⠓⠿⠚⠗⠀⠎⠠⠊⠾⠀⠕⠕⠁⠮⠀⠎⠔⠮⠀⠠⠍⠀⠕⠌⠉⠵⠫⠦⠴⠐⠮⠀⠑⠯⠎⠠⠎⠉⠵⠀⠣⠒⠀⠊⠽⠒⠊⠲",
    "조선 시대의 시인 강백(1690?~1777?)의 자는 자청이고, 호는 우곡이다.": "⠨⠥⠠⠾⠀⠠⠕⠊⠗⠺⠀⠠⠕⠟⠀⠫⠶⠘⠗⠁⠦⠄⠼⠁⠋⠊⠚⠦⠤⠤⠼⠁⠛⠛⠛⠦⠠⠴⠺⠀⠨⠉⠵⠀⠨⠰⠻⠕⠈⠥⠐⠀⠚⠥⠉⠵⠀⠍⠈⠭⠕⠊⠲",
    "우리 집 강아지가 가출(?)을 했어요.": "⠍⠐⠕⠀⠨⠕⠃⠀⠫⠶⠣⠨⠕⠫⠀⠫⠰⠯⠦⠄⠦⠠⠴⠮⠀⠚⠗⠌⠎⠬⠲",
    "최치원(857~?)은 통일 신라 말기에 이름을 떨쳤던 학자이자 문장가이다.": "⠰⠽⠰⠕⠏⠒⠦⠄⠼⠓⠑⠛⠤⠤⠦⠠⠴⠵⠀⠓⠿⠕⠂⠀⠠⠟⠐⠣⠀⠑⠂⠈⠕⠝⠀⠕⠐⠪⠢⠮⠀⠠⠊⠞⠰⠱⠌⠊⠾⠀⠚⠁⠨⠣⠕⠨⠀⠑⠛⠨⠶⠫⠕⠊⠲",
    "‘앞’이 아니라 ‘아.’이다.": "⠠⠦⠣⠲⠴⠄⠕⠀⠣⠉⠕⠐⠣⠀⠠⠦⠣⠲⠴⠄⠕⠊⠲",
    "아, 달이 밝구나!": "⠣⠐⠀⠊⠂⠕⠀⠘⠂⠁⠈⠍⠉⠖",
    "이게 누구야!": "⠕⠈⠝⠀⠉⠍⠈⠍⠜⠖",
    "꽃이 정말 아름답구나!": "⠠⠈⠥⠆⠕⠀⠨⠻⠑⠂⠀⠣⠐⠪⠢⠊⠃⠈⠍⠉⠖",
    "청춘! 이는 듣기만 하여도 가슴이 설레는 말이다.": "⠰⠻⠰⠛⠖⠀⠕⠉⠵⠀⠊⠪⠔⠈⠕⠑⠒⠀⠚⠣⠱⠊⠥⠀⠫⠠⠪⠢⠕⠀⠠⠞⠐⠝⠉⠵⠀⠑⠂⠕⠊⠲",
    "네, 할머니!": "⠉⠝⠐⠀⠚⠂⠑⠎⠉⠕⠖",
    "근면, 검소, 협동은 우리 겨레의 미덕이다.": "⠈⠵⠑⠡⠐⠀⠈⠎⠢⠠⠥⠐⠀⠚⠱⠃⠊⠿⠵⠀⠍⠐⠕⠀⠈⠱⠐⠝⠺⠀⠑⠕⠊⠹⠕⠊⠲",
    "14,314": "⠼⠁⠙⠂⠉⠁⠙",
    "소설 구성의 3요소는 인물, 사건, 배경이다.": "⠠⠥⠠⠞⠀⠈⠍⠠⠻⠺⠀⠼⠉⠬⠠⠥⠉⠵⠀⠟⠑⠯⠐⠀⠇⠈⠾⠐⠀⠘⠗⠈⠻⠕⠊⠲",
    "서울 외환시장에서 환율은 현재 달러당 1,139.6원이다.": "⠠⠎⠯⠀⠽⠚⠧⠒⠠⠕⠨⠶⠝⠠⠎⠀⠚⠧⠒⠩⠂⠵⠀⠚⠡⠨⠗⠀⠊⠂⠐⠎⠊⠶⠀⠼⠁⠂⠁⠉⠊⠲⠋⠏⠒⠕⠊⠲",
    "정치·경제": "⠨⠻⠰⠕⠐⠆⠈⠻⠨⠝",
    "사과·배, 배추·무": "⠇⠈⠧⠐⠆⠘⠗⠐⠀⠘⠗⠰⠍⠐⠆⠑⠍",
    "시장에서 사과·배·복숭아, 마늘·고추·파, 조기·명태·고등어를 샀습니다.": "⠠⠕⠨⠶⠝⠠⠎⠀⠇⠈⠧⠐⠆⠘⠗⠐⠆⠘⠭⠠⠍⠶⠣⠐⠀⠑⠉⠮⠐⠆⠈⠥⠰⠍⠐⠆⠙⠐⠀⠨⠥⠈⠕⠐⠆⠑⠻⠓⠗⠐⠆⠈⠥⠊⠪⠶⠎⠐⠮⠀⠇⠌⠠⠪⠃⠉⠕⠊⠲",
    "8·15 광복": "⠼⠓⠐⠆⠁⠑⠀⠈⠧⠶⠘⠭",
    "통권 제54·55·56호": "⠓⠿⠈⠏⠒⠀⠨⠝⠼⠑⠙⠐⠆⠑⠑⠐⠆⠑⠋⠀⠚⠥",
    "3.1 운동": "⠼⠉⠲⠁⠀⠛⠊⠿",
    "장애인·노인·임산부 등의 편의 증진 보장에 관한 법률": "⠨⠶⠗⠟⠐⠆⠉⠥⠟⠐⠆⠕⠢⠇⠒⠘⠍⠀⠊⠪⠶⠺⠀⠙⠡⠺⠀⠨⠪⠶⠨⠟⠀⠘⠥⠨⠶⠝⠀⠈⠧⠒⠚⠒⠀⠘⠎⠃⠐⠩⠂",
    # 영어 추가 후 반영 예정
    # "O·X 퀴즈": "⠴⠠⠕⠐⠆⠴⠠⠭⠲⠀⠋⠍⠗⠨⠪",
    # "KAIST·서울대 등 국내 대학 ‘아시아 최고 혁신 대학’에 대거 이름 올려": "⠴⠠⠠⠅⠁⠊⠌⠐⠆⠠⠎⠯⠊⠗⠀⠊⠪⠶⠀⠈⠍⠁⠉⠗⠀⠊⠗⠚⠁⠀⠠⠦⠣⠠⠕⠣⠀⠰⠽⠈⠥⠀⠚⠱⠁⠠⠟⠀⠊⠗⠚⠁⠠⠴⠝⠀⠊⠗⠈⠎⠀⠕⠐⠪⠢⠀⠥⠂⠐⠱",
    # "서울대·KAIST 등 국내 대학 ‘아시아 최고 혁신 대학’에 대거 이름 올려": "⠠⠎⠯⠊⠗⠐⠆⠴⠠⠠⠅⠁⠊⠌⠲⠀⠊⠪⠶⠀⠈⠍⠁⠉⠗⠀⠊⠗⠚⠁⠀⠠⠦⠣⠠⠕⠣⠀⠰⠽⠈⠥⠀⠚⠱⠁⠠⠟⠀⠊⠗⠚⠁⠠⠴⠝⠀⠊⠗⠈⠎⠀⠕⠐⠪⠢⠀⠥⠂⠐⠱",
    "지금의 경상남도·경상북도, 전라남도·전라북도, 충청남도·충청북도 지역을 예부터 삼남이라 일러 왔다.": "⠨⠕⠈⠪⠢⠺⠀⠈⠻⠇⠶⠉⠢⠊⠥⠐⠆⠈⠻⠇⠶⠘⠍⠁⠊⠥⠐⠀⠨⠾⠐⠣⠉⠢⠊⠥⠐⠆⠨⠾⠐⠣⠘⠍⠁⠊⠥⠐⠀⠰⠍⠶⠰⠻⠉⠢⠊⠥⠐⠆⠰⠍⠶⠰⠻⠘⠍⠁⠊⠥⠀⠨⠕⠱⠁⠮⠀⠌⠘⠍⠓⠎⠀⠇⠢⠉⠢⠕⠐⠣⠀⠕⠂⠐⠎⠀⠧⠌⠊⠲",
    "의 종류는 내용에 따라 서정시·서사시·극시, 형식에 따라 자유시·정형시·산문시로 나눌 수 있다.": "⠺⠀⠨⠿⠐⠩⠉⠵⠀⠉⠗⠬⠶⠝⠀⠠⠊⠐⠣⠀⠠⠎⠨⠻⠠⠕⠐⠆⠠⠎⠇⠠⠕⠐⠆⠈⠪⠁⠠⠕⠐⠀⠚⠻⠠⠕⠁⠝⠀⠠⠊⠐⠣⠀⠨⠣⠩⠠⠕⠐⠆⠨⠻⠚⠻⠠⠕⠐⠆⠇⠒⠑⠛⠠⠕⠐⠥⠀⠉⠉⠯⠀⠠⠍⠀⠕⠌⠊⠲",
    "4·19 혁명": "⠼⠙⠐⠆⠁⠊⠀⠚⠱⠁⠑⠻",
    "1919. 3. 1. 그 날의 꿈": "⠼⠁⠊⠁⠊⠲⠀⠼⠉⠲⠀⠼⠁⠲⠀⠈⠪⠀⠉⠂⠺⠀⠠⠈⠍⠢",
    "2017.5.9. 뉴스는 대통령 선거 특집으로 이루어졌다.": "⠼⠃⠚⠁⠛⠲⠑⠲⠊⠲⠀⠉⠩⠠⠪⠉⠵⠀⠊⠗⠓⠿⠐⠻⠀⠠⠾⠈⠎⠀⠓⠪⠁⠨⠕⠃⠪⠐⠥⠀⠕⠐⠍⠎⠨⠱⠌⠊⠲",
    "일시: 2006년 2월 28일 13시": "⠕⠂⠠⠕⠐⠂⠀⠼⠃⠚⠚⠋⠀⠉⠡⠀⠼⠃⠏⠂⠀⠼⠃⠓⠕⠂⠀⠼⠁⠉⠠⠕",
    "청군:백군": "⠰⠻⠈⠛⠐⠂⠘⠗⠁⠈⠛",
    "480:420": "⠼⠙⠓⠚⠐⠂⠙⠃⠚",
    "오전 10:20": "⠥⠨⠾⠀⠼⠁⠚⠐⠂⠃⠚",
    "요한 3:16": "⠬⠚⠒⠀⠼⠉⠐⠂⠁⠋",
    "문장 부호: 마침표, 물음표, 느낌표, 쉼표 등": "⠑⠛⠨⠶⠀⠘⠍⠚⠥⠐⠂⠀⠑⠰⠕⠢⠙⠬⠐⠀⠑⠯⠪⠢⠙⠬⠐⠀⠉⠪⠠⠈⠕⠢⠙⠬⠐⠀⠠⠍⠗⠢⠙⠬⠀⠊⠪⠶",
    "김 과장: 난 못 참겠다.": "⠈⠕⠢⠀⠈⠧⠨⠶⠐⠂⠀⠉⠒⠀⠑⠥⠄⠀⠰⠣⠢⠈⠝⠌⠊⠲",
    "2002년 6월 20일은 한국:미국의 월드컵 경기가 있었던 날이다.": "⠼⠃⠚⠚⠃⠀⠉⠡⠀⠼⠋⠏⠂⠀⠼⠃⠚⠕⠂⠵⠀⠚⠒⠈⠍⠁⠐⠂⠑⠕⠈⠍⠁⠺⠀⠏⠂⠊⠪⠋⠎⠃⠀⠈⠻⠈⠕⠫⠀⠕⠌⠎⠌⠊⠾⠀⠉⠂⠕⠊⠲",
    "2014 브라질 월드컵 결승전에서 독일이 1:0으로 아르헨티나를 꺾고 우승했다.": "⠼⠃⠚⠁⠙⠀⠘⠪⠐⠣⠨⠕⠂⠀⠏⠂⠊⠪⠋⠎⠃⠀⠈⠳⠠⠪⠶⠨⠾⠝⠠⠎⠀⠊⠭⠕⠂⠕⠀⠼⠁⠐⠂⠚⠪⠐⠥⠀⠣⠐⠪⠚⠝⠒⠓⠕⠉⠐⠮⠀⠠⠈⠹⠁⠈⠥⠀⠍⠠⠪⠶⠚⠗⠌⠊⠲",
    "해 뜨는 시각 7:10:54": "⠚⠗⠀⠠⠊⠪⠉⠵⠀⠠⠕⠫⠁⠀⠼⠛⠐⠂⠁⠚⠐⠂⠑⠙",
    "창세 1:1": "⠰⠣⠶⠠⠝⠀⠼⠁⠐⠂⠁",
    "두시언해 6:15": "⠊⠍⠠⠕⠾⠚⠗⠀⠼⠋⠐⠂⠁⠑",
    "상점에는 배추, 시금치, 당근과 같은 야채; 미역, 생선, 젓갈 등과 같은 수산물이 있었다.": "⠇⠶⠨⠎⠢⠝⠉⠵⠀⠘⠗⠰⠍⠐⠀⠠⠕⠈⠪⠢⠰⠕⠐⠀⠊⠶⠈⠵⠈⠧⠀⠫⠦⠵⠀⠜⠰⠗⠰⠆⠀⠑⠕⠱⠁⠐⠀⠠⠗⠶⠠⠾⠐⠀⠨⠎⠄⠫⠂⠀⠊⠪⠶⠈⠧⠀⠫⠦⠵⠀⠠⠍⠇⠒⠑⠯⠕⠀⠕⠌⠎⠌⠊⠲",
    "김정례, 2003; 이명수, 1997; 홍길동, 2005": "⠈⠕⠢⠨⠻⠐⠌⠐⠀⠼⠃⠚⠚⠉⠰⠆⠀⠕⠑⠻⠠⠍⠐⠀⠼⠁⠊⠊⠛⠰⠆⠀⠚⠿⠈⠕⠂⠊⠿⠐⠀⠼⠃⠚⠚⠑",
    "잠언 1:28; 아가 5:6": "⠨⠢⠾⠀⠼⠁⠐⠂⠃⠓⠰⠆⠀⠣⠫⠀⠼⠑⠐⠂⠋",
    "남궁만/남궁 만": "⠉⠢⠈⠍⠶⠑⠒⠸⠌⠉⠢⠈⠍⠶⠀⠑⠒",
    "착한 사람/악한 사람": "⠰⠣⠁⠚⠒⠀⠇⠐⠣⠢⠸⠌⠣⠁⠚⠒⠀⠇⠐⠣⠢",
    "사과를 그리다 보면/배가 되고/배를 그리다 보면/사과가 된다.": "⠇⠈⠧⠐⠮⠀⠈⠪⠐⠕⠊⠀⠘⠥⠑⠡⠸⠌⠘⠗⠫⠀⠊⠽⠈⠥⠸⠌⠘⠗⠐⠮⠀⠈⠪⠐⠕⠊⠀⠘⠥⠑⠡⠸⠌⠇⠈⠧⠫⠀⠊⠽⠒⠊⠲",
    "금메달/은메달/동메달": "⠈⠪⠢⠑⠝⠊⠂⠸⠌⠵⠑⠝⠊⠂⠸⠌⠊⠿⠑⠝⠊⠂",
    "100미터/초": "⠼⠁⠚⠚⠀⠑⠕⠓⠎⠸⠌⠰⠥",
    "예로부터 “민심은 천심이다.”라고 하였다.": "⠌⠐⠥⠘⠍⠓⠎⠀⠦⠑⠟⠠⠕⠢⠵⠀⠰⠾⠠⠕⠢⠕⠊⠲⠴⠐⠣⠈⠥⠀⠚⠣⠱⠌⠊⠲",
    "푯말에는 “출입 금지 구역”이라고 쓰여 있었다.": "⠙⠬⠄⠑⠂⠝⠉⠵⠀⠦⠰⠯⠕⠃⠀⠈⠪⠢⠨⠕⠀⠈⠍⠱⠁⠴⠕⠐⠣⠈⠥⠀⠠⠠⠪⠱⠀⠕⠌⠎⠌⠊⠲",
    "“여러분! 침착해야 합니다. ‘하늘이 무너져도 솟아날 구멍이 있다.’고 합니다.”": "⠦⠱⠐⠎⠘⠛⠖⠀⠰⠕⠢⠰⠣⠁⠚⠗⠜⠀⠚⠃⠉⠕⠊⠲⠀⠠⠦⠚⠉⠮⠕⠀⠑⠍⠉⠎⠨⠱⠊⠥⠀⠠⠥⠄⠣⠉⠂⠀⠈⠍⠑⠎⠶⠕⠀⠕⠌⠊⠲⠴⠄⠈⠥⠀⠚⠃⠉⠕⠊⠲⠴",
    "그는 “여러분! ‘시작이 반이다.’라는 말 들어 보셨죠?”라고 말하며 강연을 시작했다.": "⠈⠪⠉⠵⠀⠦⠱⠐⠎⠘⠛⠖⠀⠠⠦⠠⠕⠨⠁⠕⠀⠘⠒⠕⠊⠲⠴⠄⠐⠣⠉⠵⠀⠑⠂⠀⠊⠮⠎⠀⠘⠥⠠⠱⠌⠨⠬⠦⠴⠐⠣⠈⠥⠀⠑⠂⠚⠑⠱⠀⠫⠶⠡⠮⠀⠠⠕⠨⠁⠚⠗⠌⠊⠲",
    "나는 ‘일이 다 틀렸나 보군.’ 하고 생각하였다.": "⠉⠉⠵⠀⠠⠦⠕⠂⠕⠀⠊⠀⠓⠮⠐⠱⠌⠉⠀⠘⠥⠈⠛⠲⠴⠄⠀⠚⠈⠥⠀⠠⠗⠶⠫⠁⠚⠣⠱⠌⠊⠲",
    "니체(독일의 철학자)는 이렇게 말했다.": "⠉⠕⠰⠝⠦⠄⠊⠭⠕⠂⠺⠀⠰⠞⠚⠁⠨⠠⠴⠉⠵⠀⠕⠐⠎⠴⠈⠝⠀⠑⠂⠚⠗⠌⠊⠲",
    "니체(독일의 철학자)의 말을 빌리면 다음과 같다.": "⠉⠕⠰⠝⠦⠄⠊⠭⠕⠂⠺⠀⠰⠞⠚⠁⠨⠠⠴⠺⠀⠑⠂⠮⠀⠘⠕⠂⠐⠕⠑⠡⠀⠊⠣⠪⠢⠈⠧⠀⠫⠦⠊⠲",
    "종묘(제례)악은 종묘에서 역대 제왕의 제사 때 쓰던 음악이다.": "⠨⠿⠑⠬⠦⠄⠨⠝⠐⠌⠠⠴⠣⠁⠵⠀⠨⠿⠑⠬⠝⠠⠎⠀⠱⠁⠊⠗⠀⠨⠝⠧⠶⠺⠀⠨⠝⠇⠀⠠⠊⠗⠀⠠⠠⠪⠊⠾⠀⠪⠢⠣⠁⠕⠊⠲",
    "현우: (가쁜 숨을 내쉬며) 왜 이렇게 빨리 뛰어?": "⠚⠡⠍⠐⠂⠀⠦⠄⠫⠠⠘⠵⠀⠠⠍⠢⠮⠀⠉⠗⠠⠍⠗⠑⠱⠠⠴⠀⠧⠗⠀⠕⠐⠎⠴⠈⠝⠀⠠⠘⠂⠐⠕⠀⠠⠊⠍⠗⠎⠦",
    "아이들이 모두 학교{에, 로, 까지} 갔어요.": "⠣⠕⠊⠮⠕⠀⠑⠥⠊⠍⠀⠚⠁⠈⠬⠦⠂⠝⠐⠀⠐⠥⠐⠀⠠⠫⠨⠕⠐⠴⠀⠫⠌⠎⠬⠲",
    "나이[연세]": "⠉⠣⠕⠦⠆⠡⠠⠝⠰⠴",
    "낱말[단어]": "⠉⠦⠑⠂⠦⠆⠊⠒⠎⠰⠴",
    "수족[손발]": "⠠⠍⠨⠭⠦⠆⠠⠷⠘⠂⠰⠴",
    "꽃망울[꼰망울]": "⠠⠈⠥⠆⠑⠶⠯⠦⠆⠠⠈⠷⠑⠶⠯⠰⠴",
    "몫몫이[몽목씨]": "⠑⠭⠄⠑⠭⠄⠕⠦⠆⠑⠿⠑⠭⠠⠠⠕⠰⠴",
    "앞마당[암마당]": "⠣⠲⠑⠊⠶⠦⠆⠣⠢⠑⠊⠶⠰⠴",
    "이번 회의에는 두 명[이혜정(실장), 박철용(과장)]만 빼고 모두 참석했습니다.": "⠕⠘⠾⠀⠚⠽⠺⠝⠉⠵⠀⠊⠍⠀⠑⠻⠦⠆⠕⠚⠌⠨⠻⠦⠄⠠⠕⠂⠨⠶⠠⠴⠐⠀⠘⠁⠰⠞⠬⠶⠦⠄⠈⠧⠨⠶⠠⠴⠰⠴⠑⠒⠀⠠⠘⠗⠈⠥⠀⠑⠥⠊⠍⠀⠰⠣⠢⠠⠹⠚⠗⠌⠠⠪⠃⠉⠕⠊⠲",
    "그런 일은 결코 있을 수 없다.[원문에는 ‘업다’임.]": "⠈⠪⠐⠾⠀⠕⠂⠵⠀⠈⠳⠋⠥⠀⠕⠌⠮⠀⠠⠍⠀⠎⠃⠄⠊⠲⠦⠆⠏⠒⠑⠛⠝⠉⠵⠀⠠⠦⠎⠃⠊⠴⠄⠕⠢⠲⠰⠴",
    "육개장[육깨장]": "⠩⠁⠈⠗⠨⠶⠦⠆⠩⠁⠠⠈⠗⠨⠶⠰⠴",
    "우리나라 최초의 민간 신문은 『독립신문』이다.": "⠍⠐⠕⠉⠐⠣⠀⠰⠽⠰⠥⠺⠀⠑⠟⠫⠒⠀⠠⠟⠑⠛⠵⠀⠰⠦⠊⠭⠐⠕⠃⠠⠟⠑⠛⠴⠆⠕⠊⠲",
    "《훈민정음》은 유네스코 세계 기록 유산으로 지정되었다.": "⠰⠦⠚⠛⠑⠟⠨⠻⠪⠢⠴⠆⠵⠀⠩⠉⠝⠠⠪⠋⠥⠀⠠⠝⠈⠌⠀⠈⠕⠐⠭⠀⠩⠇⠒⠪⠐⠥⠀⠨⠕⠨⠻⠊⠽⠎⠌⠊⠲",
    "박경리의 『토지』는 전 5부 16권에 이르는 대하소설이다.": "⠘⠁⠈⠻⠐⠕⠺⠀⠰⠦⠓⠥⠨⠕⠴⠆⠉⠵⠀⠨⠾⠀⠼⠑⠘⠍⠀⠼⠁⠋⠈⠏⠒⠝⠀⠕⠐⠪⠉⠵⠀⠊⠗⠚⠠⠥⠠⠞⠕⠊⠲",
    "윤동주의 유고 시집인 《하늘과 바람과 별과 시》에는 31편의 시가 실려 있다.": "⠩⠒⠊⠿⠨⠍⠺⠀⠩⠈⠥⠀⠠⠕⠨⠕⠃⠟⠀⠰⠦⠚⠉⠮⠈⠧⠀⠘⠐⠣⠢⠈⠧⠀⠘⠳⠈⠧⠀⠠⠕⠴⠆⠝⠉⠵⠀⠼⠉⠁⠀⠙⠡⠺⠀⠠⠕⠫⠀⠠⠕⠂⠐⠱⠀⠕⠌⠊⠲",
    "이 곡은 베르디가 작곡한 「축배의 노래」이다.": "⠕⠀⠈⠭⠵⠀⠘⠝⠐⠪⠊⠕⠫⠀⠨⠁⠈⠭⠚⠒⠀⠐⠦⠰⠍⠁⠘⠗⠺⠀⠉⠥⠐⠗⠴⠂⠕⠊⠲",
    "현행 <국어의 로마자 표기법>은 2000년에 고시된 것이다.": "⠚⠡⠚⠗⠶ ⠐⠦⠈⠍⠁⠎⠺ ⠐⠥⠑⠨ ⠙⠬⠈⠕⠘⠎⠃⠴⠂⠵ ⠼⠃⠚⠚⠚ ⠉⠡⠝ ⠈⠥⠠⠕⠊⠽⠒ ⠸⠎⠕⠊⠲",
    "추사 김정희의 〈세한도〉는 절세의 명작이다.": "⠰⠍⠇⠀⠈⠕⠢⠨⠻⠚⠺⠺⠀⠐⠦⠠⠝⠚⠒⠊⠥⠴⠂⠉⠵⠀⠨⠞⠠⠝⠺⠀⠑⠻⠨⠁⠕⠊⠲",
    "이 곡은 베토벤이 작곡한 「운명 교향곡」이다.": "⠕⠀⠈⠭⠵⠀⠘⠝⠓⠥⠘⠝⠒⠕⠀⠨⠁⠈⠭⠚⠒⠀⠐⠦⠛⠑⠻⠀⠈⠬⠚⠜⠶⠈⠭⠴⠂⠕⠊⠲",
    "겨울‐나그네": "⠈⠱⠯⠤⠉⠈⠪⠉⠝",
    "불‐구경": "⠘⠯⠤⠈⠍⠈⠻",
    "손‐발": "⠠⠷⠤⠘⠂",
    "이 논문은 서론‐본론‐결론을 통일성 있게 잘 쓴 글이다.": "⠕⠀⠉⠷⠑⠛⠵⠀⠠⠎⠐⠷⠤⠘⠷⠐⠷⠤⠈⠳⠐⠷⠮⠀⠓⠿⠕⠂⠠⠻⠀⠕⠌⠈⠝⠀⠨⠂⠀⠠⠠⠵⠀⠈⠮⠕⠊⠲",
    "원‐달러 환율": "⠏⠒⠤⠊⠂⠐⠎⠀⠚⠧⠒⠩⠂",
    "사과―과일의 일종―는 빨간색이다.": "⠇⠈⠧⠤⠤⠈⠧⠕⠂⠺⠀⠕⠂⠨⠿⠤⠤⠉⠵⠀⠠⠘⠂⠫⠒⠠⠗⠁⠕⠊⠲",
    "내가 아침마다 먹는 오렌지―과일의 일종―는 노란색이다.": "⠉⠗⠫⠀⠣⠰⠕⠢⠑⠊⠀⠑⠹⠉⠵⠀⠥⠐⠝⠒⠨⠕⠤⠤⠈⠧⠕⠂⠺⠀⠕⠂⠨⠿⠤⠤⠉⠵⠀⠉⠥⠐⠣⠒⠠⠗⠁⠕⠊⠲",
    "본 토론회의 제목은 ‘역사 바로잡기―근대의 설정’이다.": "⠘⠷⠀⠓⠥⠐⠷⠚⠽⠺⠀⠨⠝⠑⠭⠵⠀⠠⠦⠱⠁⠇⠀⠘⠐⠥⠨⠃⠈⠕⠤⠤⠈⠵⠊⠗⠺⠀⠠⠞⠨⠻⠴⠄⠕⠊⠲",
    "나는―솔직히 말하면―그 말이 별로 탐탁지 않아.": "⠉⠉⠵⠤⠤⠠⠥⠂⠨⠕⠁⠚⠕⠀⠑⠂⠚⠑⠡⠤⠤⠈⠪⠀⠑⠂⠕⠀⠘⠳⠐⠥⠀⠓⠢⠓⠁⠨⠕⠀⠣⠒⠴⠣⠲",
    "치열한 접전 끝에 우리 팀은 ― 다시 생각하기도 싫지만 ― 결국 지고 말았다.": "⠰⠕⠳⠚⠒⠀⠨⠎⠃⠨⠾⠀⠠⠈⠪⠦⠝⠀⠍⠐⠕⠀⠓⠕⠢⠵⠀⠤⠤⠀⠊⠠⠕⠀⠠⠗⠶⠫⠁⠚⠈⠕⠊⠥⠀⠠⠕⠂⠴⠨⠕⠑⠒⠀⠤⠤⠀⠈⠳⠈⠍⠁⠀⠨⠕⠈⠥⠀⠑⠂⠣⠌⠊⠲",
    "올해의 권장 도서는 톨스토이의 『인생이란 무엇인가 ― 삶의 길 ―』이다.": "⠥⠂⠚⠗⠺⠀⠈⠏⠒⠨⠶⠀⠊⠥⠠⠎⠉⠵⠀⠓⠥⠂⠠⠪⠓⠥⠕⠺⠀⠰⠦⠟⠠⠗⠶⠕⠐⠣⠒⠀⠑⠍⠎⠄⠟⠫⠀⠤⠤⠀⠇⠂⠢⠺⠀⠈⠕⠂⠀⠤⠤⠴⠆⠕⠊⠲",
    "김 교수는 ‘풍성한 언어생활―표준어와 방언’이라는 주제로 특강을 할 예정이다.": "⠈⠕⠢⠀⠈⠬⠠⠍⠉⠵⠀⠠⠦⠙⠍⠶⠠⠻⠚⠒⠀⠾⠎⠠⠗⠶⠚⠧⠂⠤⠤⠙⠬⠨⠛⠎⠧⠀⠘⠶⠾⠴⠄⠕⠐⠣⠉⠵⠀⠨⠍⠨⠝⠐⠥⠀⠓⠪⠁⠫⠶⠮⠀⠚⠂⠀⠌⠨⠻⠕⠊⠲",
    "9월 15일~9월 25일": "⠼⠊⠏⠂⠀⠼⠁⠑⠕⠂⠤⠤⠼⠊⠏⠂⠀⠼⠃⠑⠕⠂",
    "~운동": "⠤⠤⠛⠊⠿",
    "~노래": "⠤⠤⠉⠥⠐⠗",
    "서울~천안 정도는 출퇴근이 가능하다.": "⠠⠎⠯⠤⠤⠰⠾⠣⠒⠀⠨⠻⠊⠥⠉⠵⠀⠰⠯⠓⠽⠈⠵⠕⠀⠫⠉⠪⠶⠚⠊⠲",
    "“어디 나하고 한번…….” 하고 철수가 나섰다.": "⠦⠎⠊⠕⠀⠉⠚⠈⠥⠀⠚⠒⠘⠾⠠⠠⠠⠲⠴⠀⠚⠈⠥⠀⠰⠞⠠⠍⠫⠀⠉⠠⠎⠌⠊⠲",
    "그는 최선을 다했다. 그러나 성공할지는…….": "⠈⠪⠉⠵ ⠰⠽⠠⠾⠮ ⠊⠚⠗⠌⠊⠲ ⠁⠉ ⠠⠻⠈⠿⠚⠂⠨⠕⠉⠵⠠⠠⠠⠲",
    "* 야애: 들에 낀 안개": "⠔⠔⠀⠜⠤⠗⠐⠂⠀⠊⠮⠝⠀⠠⠈⠟⠀⠣⠒⠈⠗",
    "가우디의 건축물들은 자연에서 작품의 모티프*를 따와 대부분 수학적인 곡선이 주를 이룬다.": "⠫⠍⠊⠕⠺⠀⠈⠾⠰⠍⠁⠑⠯⠊⠮⠵⠀⠨⠣⠡⠝⠠⠎⠀⠨⠁⠙⠍⠢⠺⠀⠑⠥⠓⠕⠙⠪⠔⠔⠐⠮⠀⠠⠊⠣⠧⠀⠊⠗⠘⠍⠘⠛⠀⠠⠍⠚⠁⠨⠹⠟⠀⠈⠭⠠⠾⠕⠀⠨⠍⠐⠮⠀⠕⠐⠛⠊⠲",
    "* 연도는 1년 단위임.": "⠔⠔⠀⠡⠊⠥⠉⠵⠀⠼⠁⠀⠉⠡⠀⠊⠒⠍⠗⠕⠢⠲",
    "※ 확인 사항": "⠔⠔⠀⠚⠧⠁⠟⠀⠇⠚⠶",
    "* 1번부터 17번까지는 듣고 답하는 문제입니다.": "⠔⠔⠀⠼⠁⠘⠾⠘⠍⠓⠎⠀⠼⠁⠛⠘⠾⠠⠫⠨⠕⠉⠵⠀⠊⠪⠔⠈⠥⠀⠊⠃⠚⠉⠵⠀⠑⠛⠨⠝⠕⠃⠉⠕⠊⠲",
    "※ 답안지의 각 장마다 교시, 영역, 성명과 수험 번호를 쓰고, 답을 정확히 기입하시오.": "⠔⠔⠀⠊⠃⠣⠒⠨⠕⠺⠀⠫⠁⠀⠨⠶⠑⠊⠀⠈⠬⠠⠕⠐⠀⠻⠱⠁⠐⠀⠠⠻⠑⠻⠈⠧⠀⠠⠍⠚⠎⠢⠀⠘⠾⠚⠥⠐⠮⠀⠠⠠⠪⠈⠥⠐⠀⠊⠃⠮⠀⠨⠻⠚⠧⠁⠚⠕⠀⠈⠕⠕⠃⠚⠠⠕⠥⠲",
    "최근에는 확대 가족은 많이 줄어들고 대부분이 부부 중심의 핵가족*을 이루고 있다.": "⠰⠽⠈⠵⠝⠉⠵⠀⠚⠧⠁⠊⠗⠀⠫⠨⠭⠵⠀⠑⠒⠴⠕⠀⠨⠯⠎⠊⠮⠈⠥⠀⠊⠗⠘⠍⠘⠛⠕⠀⠘⠍⠘⠍⠀⠨⠍⠶⠠⠕⠢⠺⠀⠚⠗⠁⠫⠨⠭⠔⠔⠮⠀⠕⠐⠍⠈⠥⠀⠕⠌⠊⠲",
    "파란 구슬 빛 바탕에 자줏빛 호장*을 받친 호장저고리": "⠙⠐⠣⠒⠀⠈⠍⠠⠮⠀⠘⠕⠆⠀⠘⠓⠶⠝⠀⠨⠨⠍⠄⠘⠕⠆⠀⠚⠥⠨⠶⠔⠔⠮⠀⠘⠔⠰⠟⠀⠚⠥⠨⠶⠨⠎⠈⠥⠐⠕",
    "ʼ88 서울 올림픽": "⠼⠄⠓⠓⠀⠠⠎⠯⠀⠥⠂⠐⠕⠢⠙⠕⠁",
    "ʼ17 개정 한국 점자 규정": "⠼⠄⠁⠛⠀⠈⠗⠨⠻⠀⠚⠒⠈⠍⠁⠀⠨⠎⠢⠨⠀⠈⠩⠨⠻",
    "(02) 222‐7777~8": "⠦⠄⠼⠚⠃⠠⠴⠀⠼⠃⠃⠃⠤⠛⠛⠛⠛⠤⠤⠼⠓",
    "90~100점": "⠼⠊⠚⠤⠤⠼⠁⠚⠚⠨⠎⠢",
    "(02) 123‐4567~8": "⠦⠄⠼⠚⠃⠠⠴⠀⠼⠁⠃⠉⠤⠙⠑⠋⠛⠤⠤⠼⠓",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",

}

def testTran():
    """
    테스트 케이스에 저장된 문자를 번역하여
    올바른 점자와 비교,
        :return: 틀린 번역의 경우, 번역과 올바른 점자를 출력
    """
    total = 0
    for tc in translateTestCase:
        try:
            result = translate(tc)
            answer = translateTestCase[tc]
            cnt = 0
            for (r, a) in zip(result, answer.replace("⠀", " ")):
                if (r == a): cnt += 1
            if (cnt == len(result)):
                total += 1
            else:
                print("ERR ===============")
                print(f"TEST CAST : {tc}")
                print(f"result : {result}")
                print(f"answer : {answer}")
                print("===================")
        except:
            print(f"번역 오류 : {tc}")

    print(f"번역 일치율 {total / len(translateTestCase) * 100}")

## 테스트 실행
testTran()