# -*- coding: utf-8 -*-
"""
GitHub Issue作成スクリプト（シンプル版）
"""

import json
import urllib.request
import urllib.parse
import os

REPO_OWNER = "boobeem2000"
REPO_NAME = "-"
GITHUB_API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"

title = "集客アイデア: SNSから見込み客を発見して個別相談に繋ぐAI DMフロー"

body = """## アイデア概要

見込み客をSNSから見つけてきて、その人にAIで作ったDMを作って個別相談に流れるフローを作る

---

## 詳細

### 目的
- SNS（Instagram、Twitter、Facebookなど）から見込み客を発見
- AIを使ってパーソナライズされたDMを作成
- 個別相談への導線を構築

### フロー
1. **見込み客の発見**
   - SNSでターゲットとなるユーザーを特定
   - キーワード検索、ハッシュタグ検索などを活用
   - プロフィールや投稿内容からニーズを分析

2. **AIによるDM作成**
   - 見込み客の情報を分析
   - パーソナライズされたDM文面を自動生成
   - トーンやスタイルを調整

3. **個別相談への導線**
   - DMから自然に個別相談に誘導
   - 予約システムへのリンク
   - フォローアップの自動化

---

## 実装要件

### 必要な機能
- [ ] SNSアカウント連携
- [ ] 見込み客の自動検索機能
- [ ] AIによるDM文面生成
- [ ] DM送信の自動化（手動承認あり）
- [ ] 個別相談への予約システム連携
- [ ] フォローアップの自動化

### 使用技術
- AI API (OpenAI, Claude等)
- SNS API連携
- 自動化ツール
- 予約システム連携

---

## 期待される効果

- 集客効率の向上
- パーソナライズされたアプローチによる成約率向上
- 時間の削減
- スケーラビリティの向上

---

## 次のステップ

1. 使用するSNSプラットフォームの選定
2. AI APIの選定と設定
3. プロトタイプの開発
4. テスト運用
5. 本格運用開始

---

## 関連Issue

- #1 - ひとあかり（ゲスト用専用ラインアプリ）
"""

data = {
    "title": title,
    "body": body,
    "labels": ["集客", "アイデア", "enhancement"]
}

data_json = json.dumps(data, ensure_ascii=False).encode('utf-8')

# 環境変数からトークンを取得
token = os.environ.get("GITHUB_TOKEN")

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json",
}

if token:
    headers["Authorization"] = f"token {token}"
    print("GitHub APIを使用してIssueを作成します...")
    try:
        req = urllib.request.Request(GITHUB_API_URL, data=data_json, headers=headers)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"Issue作成成功！")
            print(f"Issue URL: {result['html_url']}")
            print(f"Issue #: {result['number']}")
    except urllib.error.HTTPError as e:
        print(f"エラー: {e.code} - {e.reason}")
        if e.code == 401:
            print("\nGitHub Personal Access Tokenが必要です。")
            print("トークンを取得する方法:")
            print("1. https://github.com/settings/tokens にアクセス")
            print("2. 'Generate new token (classic)' をクリック")
            print("3. 'repo' スコープを選択")
            print("4. トークンを生成して環境変数 GITHUB_TOKEN に設定")
        error_body = e.read().decode('utf-8')
        print(f"エラー詳細: {error_body}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
else:
    print("GitHub Personal Access Tokenが設定されていません。")
    print("\n以下の方法でIssueを作成できます：")
    print("\n1. GitHubのWeb UIで作成:")
    print(f"   https://github.com/{REPO_OWNER}/{REPO_NAME}/issues/new")
    print("\n2. 以下の内容をコピー＆ペーストしてください：")
    print("\n" + "="*60)
    print("タイトル:")
    print(title)
    print("\n本文:")
    print(body)
    print("="*60)

