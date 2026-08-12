import json
import os

# 파일 경로 및 내보내기 디렉터리 정의
DATA_FILE = "prompts.json"
EXPORT_DIR = "exports"

# 기본 프롬프트 데이터 (prompts.json 파일이 없을 때 초기화용)
DEFAULT_PROMPTS = [
    {
        "id": 1,
        "title": "하이브 신인개발팀 월말 평가 보고서 작성",
        "category": "페르소나",
        "content": "너는 하이브 10년 차 수석 평가자야. 트레이너 피드백을 바탕으로 환각 없이 명사형(~함, ~임) 종결 보고서를 작성하고, 모호한 정보는 [확인 필요] 처리해줘.",
        "favorite": True
    },
    {
        "id": 2,
        "title": "혼궁(Hon-Gung) 브랜드 영상 AI 통합 생성 파이프라인",
        "category": "멀티모달",
        "content": "[비주얼] Cinematic framing shot, Gyeongbokgung 경회루, 저승사자 컨셉의 한복 착용 아이돌 캐릭터가 걸어오는 장면.\n[최적화] AI 형태 붕괴 방지를 위해 과도한 스타일을 제외하고 대칭 구도와 조명 대비에 집중.\n[파이프라인] Nato(스케치) -> Firefly(디테일) -> Runway(카메라 줌인) -> Suno(사운드) 연동 10초 브랜드 필름 구성.",
        "favorite": True
    },
    {
        "id": 3,
        "title": "고립청년 신청서 자동 수집 및 노션 DB 연동",
        "category": "자동화",
        "content": "구글 시트(Watch New Rows)로 고립청년 신청 데이터를 수집하고, 노션에 청년별 독립 상세 페이지를 생성하여 상담 이력 및 '심각/일반' 위험도를 체계적으로 보관하는 모니터링 워크플로우 구축.",
        "favorite": True
    },
    {
        "id": 4,
        "title": "유기동물 입양 홍보 문구 생성 및 시급성별 이메일 자동 발송",
        "category": "자동화",
        "content": "노션/구글 시트에 신규 유기동물 입력 시 AI(Gemini)가 홍보 문구를 작성하고, 입양 시급성(급구/일반)에 따라 분기(Router) 처리하여 맞춤형 메일을 자동 발송하는 골든타임 확보 워크플로우 구축.",
        "favorite": True
    }
]

def load_prompts():
    """prompts.json 파일에서 데이터를 불러오는 함수 (영속화: Read)"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ 파일 불러오기 실패 ({e}). 기본 데이터를 사용합니다.")
            return DEFAULT_PROMPTS.copy()
    else:
        # 파일이 없으면 기본 데이터로 생성 후 저장
        save_prompts(DEFAULT_PROMPTS)
        return DEFAULT_PROMPTS.copy()

def save_prompts(data):
    """prompts.json 파일에 데이터를 저장하는 함수 (영속화: Write)"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"⚠️ 파일 저장 실패: {e}")

# 시작 시 JSON 데이터 로드
prompts = load_prompts()

def show_menu():
    """메뉴 출력 함수"""
    print("\n" + "=" * 45)
    print("      📝 프롬프트 관리 프로그램 (Prompt Manager)")
    print("=" * 45)
    print("1. 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 토글 (설정/해제)")
    print("7. 즐겨찾기 목록 보기")
    print("8. 카테고리별 Markdown 내보내기 [보너스 1]")
    print("0. 종료")
    print("=" * 45)

def add_prompt():
    """1. 프롬프트 추가"""
    print("\n--- [1. 프롬프트 추가] ---")
    title = input("제목을 입력하세요: ").strip()
    
    print("\n[카테고리 예시: 텍스트 생성, 이미지 생성, 영상 생성, 페르소나, 자동화, 멀티모달, 기타]")
    category = input("카테고리를 입력하세요: ").strip()
    content = input("프롬프트 내용을 입력하세요: ").strip()
    
    if not title or not category or not content:
        print("⚠️ 모든 항목을 입력해야 합니다.")
        return

    new_id = max([p["id"] for p in prompts], default=0) + 1
    prompts.append({
        "id": new_id,
        "title": title,
        "category": category,
        "content": content,
        "favorite": False
    })
    save_prompts(prompts)  # 파일 저장 (영속화)
    print(f"✅ 프롬프트가 성공적으로 추가되었으며 JSON 파일에 저장되었습니다! (ID: {new_id})")

def list_prompts(target_list=None, header="전체 목록"):
    """2. 목록 보기 공통 함수"""
    target = target_list if target_list is not None else prompts
    print(f"\n--- [{header}] (총 {len(target)}개) ---")
    if not target:
        print("등록된 프롬프트가 없습니다.")
        return

    for p in target:
        fav_mark = "★" if p["favorite"] else "☆"
        print(f"[{p['id']}] [{p['category']}] {p['title']} {fav_mark}")

def filter_by_category():
    """3. 카테고리별 조회"""
    print("\n--- [3. 카테고리별 조회] ---")
    category = input("조회할 카테고리를 입력하세요 (예: 페르소나, 멀티모달, 자동화 등): ").strip()
    filtered = [p for p in prompts if p["category"].lower() == category.lower()]
    list_prompts(filtered, f"카테고리: {category}")

def search_prompts():
    """4. 프롬프트 검색"""
    print("\n--- [4. 프롬프트 검색] ---")
    keyword = input("검색어를 입력하세요 (제목/내용): ").strip().lower()
    if not keyword:
        print("⚠️ 검색어를 입력해주세요.")
        return
    filtered = [p for p in prompts if keyword in p["title"].lower() or keyword in p["content"].lower()]
    list_prompts(filtered, f"검색어: '{keyword}'")

def view_detail():
    """5. 상세 보기"""
    print("\n--- [5. 상세 보기] ---")
    try:
        p_id = int(input("상세히 볼 프롬프트 ID를 입력하세요: "))
    except ValueError:
        print("⚠️ 올바른 숫자 ID를 입력해주세요.")
        return

    prompt = next((p for p in prompts if p["id"] == p_id), None)
    if not prompt:
        print("⚠️ 해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    fav_str = "설정됨 (★)" if prompt["favorite"] else "해제됨 (☆)"
    print("-" * 40)
    print(f"ID       : {prompt['id']}")
    print(f"제목     : {prompt['title']}")
    print(f"카테고리 : {prompt['category']}")
    print(f"즐겨찾기 : {fav_str}")
    print(f"내용     :\n{prompt['content']}")
    print("-" * 40)

def toggle_favorite():
    """6. 즐겨찾기 토글"""
    print("\n--- [6. 즐겨찾기 토글] ---")
    try:
        p_id = int(input("즐겨찾기 상태를 변경할 프롬프트 ID를 입력하세요: "))
    except ValueError:
        print("⚠️ 올바른 숫자 ID를 입력해주세요.")
        return

    prompt = next((p for p in prompts if p["id"] == p_id), None)
    if not prompt:
        print("⚠️ 해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    prompt["favorite"] = not prompt["favorite"]
    save_prompts(prompts)  # 파일 저장 (영속화)
    status = "★ 즐겨찾기 등록" if prompt["favorite"] else "☆ 즐겨찾기 해제"
    print(f"✅ [{prompt['title']}] 프롬프트가 {status}되었습니다.")

def list_favorites():
    """7. 즐겨찾기 목록 보기"""
    fav_list = [p for p in prompts if p["favorite"]]
    list_prompts(fav_list, "즐겨찾기 목록")

def export_to_markdown():
    """8. 카테고리별 Markdown 내보내기 [보너스 1]"""
    print("\n--- [8. 카테고리별 Markdown 내보내기] ---")
    if not prompts:
        print("⚠️ 내보낼 프롬프트 데이터가 없습니다.")
        return

    # exports/ 디렉터리가 없으면 자동 생성
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)

    # 카테고리별 그룹화
    categories = {}
    for p in prompts:
        cat = p["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(p)

    # 카테고리별 파일 내보내기
    exported_files = []
    for cat, item_list in categories.items():
        safe_filename = f"{cat.replace('/', '_')}.md"
        file_path = os.path.join(EXPORT_DIR, safe_filename)

        md_content = f"# 📁 {cat} 프롬프트 모음\n\n"
        md_content += f"> 총 **{len(item_list)}개**의 프롬프트가 포함되어 있습니다.\n\n---\n\n"

        for p in item_list:
            fav_str = "★" if p["favorite"] else "☆"
            md_content += f"## {p['id']}. {p['title']} [{fav_str}]\n"
            md_content += f"```text\n{p['content']}\n```\n\n---\n\n"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        exported_files.append(safe_filename)

    print(f"✅ 총 {len(exported_files)}개의 Markdown 파일이 '{EXPORT_DIR}/' 폴더에 성공적으로 저장되었습니다!")
    for fname in exported_files:
        print(f" - {EXPORT_DIR}/{fname}")

def main():
    while True:
        show_menu()
        choice = input("선택할 기능 번호를 입력하세요 (0-8): ").strip()
        
        if choice == "1":
            add_prompt()
        elif choice == "2":
            list_prompts()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            search_prompts()
        elif choice == "5":
            view_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            list_favorites()
        elif choice == "8":
            export_to_markdown()
        elif choice == "0":
            print("\n프로그램을 종료합니다. 이용해주셔서 감사합니다!")
            break
        else:
            print("\n⚠️ 잘못된 입력입니다. 메뉴 항목에 있는 번호(0~8)를 입력해 주세요.")

if __name__ == "__main__":
    main()