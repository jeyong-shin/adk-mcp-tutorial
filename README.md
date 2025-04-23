# Google ADK MCP (Model Context Protocol) Tutorial

이 저장소는 Google ADK(Agent Development Kit)에서 MCP(Model Context Protocol)를 사용하는 두 가지 예시를 포함하고 있습니다.

## 개요

본 프로젝트는 다음과 같은 MCP 예시를 제공합니다:

1. **Blender MCP** - 3D 모델링 소프트웨어인 Blender를 제어하기 위한 MCP 예시
2. **Obsidian MCP** - 노트 테이킹 앱 Obsidian을 Google 검색과 함께 활용하는 MCP 예시

## 폴더 구조

```
.
├── mcp_blender/       # Blender MCP 예시 코드
├── mcp_obsidian/      # Obsidian MCP와 Google Search 연동 예시 코드
├── .env.example       # 환경 변수 예시 파일
├── requirements.txt   # 필요한 패키지 목록
└── README.md          # 프로젝트 설명 문서
```

## 시작하기

### 필수 요구사항

- Python 3.9+
- uv
- Google API 키
- Anthropic API 키
- Blender (mcp_blender 예시용)
- Obsidian (mcp_obsidian 예시용)

### 설치 및 실행 방법

1. 환경 변수 설정
   ```bash
   cp .env.example .env
   ```
   `.env` 파일을 열어 API 키와 호스트 정보를 입력하세요.

2. 가상 환경 생성
   ```bash
   python -m venv venv
   ```

3. 필요한 패키지 설치
   ```bash
   pip install google-adk litellm
   ```

4. 가상 환경 활성화
   - Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     .\venv\Scripts\Activate.bat
     ```

5. ADK 웹 서버 실행
   ```bash
   adk web
   ```

## 예시 설명

### 필수 사항

두 예시 모두 uv를 설치해야 실행이 가능합니다.

Mac

```bash
brew install uv
```

Windows

```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" 
set Path=C:\Users\nntra\.local\bin;%Path%
```


### Blender MCP 예시 (`mcp_blender`)

Blender MCP 예시는 AI 에이전트가 Blender 소프트웨어를 제어하여 3D 모델링 작업을 수행하는 방법을 보여줍니다. 이 예시를 통해 텍스트 명령을 Blender 작업으로 변환하는 과정을 확인할 수 있습니다.
Blender MCP를 실행하기 위해서는 Blender와 Blender MCP Addon이 설치되어 있어야 합니다.

Blender MCP Addon은 [링크](https://github.com/ahujasid/blender-mcp)에서 `addon.py` 파일을 다운로드 받아 설치하시면 됩니다.

### Obsidian MCP 예시 (`mcp_obsidian`)

Obsidian MCP 예시는 노트 테이킹 앱인 Obsidian을 Google 검색과 함께 활용하는 방법을 보여줍니다. 이 예시를 사용하면 검색 결과를 바탕으로 Obsidian 노트를 생성하거나 업데이트하는 작업을 자동화할 수 있습니다.

이를 위해서는 Obsidian Local REST API 플러그인을 설치해야 합니다. 설치 & 활성화 후에는 `.env`파일에 `OBSIDIAN_API_KEY`와 `OBSIDIAN_HOST`를 작성해 주어야 합니다.

## 문제 해결

실행 중 문제가 발생하면 다음을 확인하세요:
- API 키와 호스트 정보가 올바르게 설정되었는지 확인
- 필요한 모든 패키지가 설치되었는지 확인
- 가상 환경이 활성화되었는지 확인
- uv가 잘 설치되었는지 확인

## 라이선스

이 프로젝트는 [LICENSE](LICENSE)에 따라 배포됩니다.
