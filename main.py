# 기본 프롬프트 데이터 (혼궁 브랜드 통합 적용 - 총 4개)
prompts = [
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
    print(f"✅ 프롬프트가 성공적으로 추가되었습니다! (ID: {new_id})")

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
    status = "★ 즐겨찾기 등록" if prompt["favorite"] else "☆ 즐겨찾기 해제"
    print(f"✅ [{prompt['title']}] 프롬프트가 {status}되었습니다.")

def list_favorites():
    """7. 즐겨찾기 목록 보기"""
    fav_list = [p for p in prompts if p["favorite"]]
    list_prompts(fav_list, "즐겨찾기 목록")

def main():
    while True:
        show_menu()
        choice = input("선택할 기능 번호를 입력하세요 (0-7): ").strip()
        
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
        elif choice == "0":
            print("\n프로그램을 종료합니다. 이용해주셔서 감사합니다!")
            break
        else:
            print("\n⚠️ 잘못된 입력입니다. 메뉴 항목에 있는 번호(0~7)를 입력해 주세요.")

if __name__ == "__main__":
    main()
    