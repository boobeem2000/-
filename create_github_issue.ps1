# GitHub Issue作成スクリプト
# 使用方法: .\create_github_issue.ps1

$owner = "boobeem2000"
$repo = "-"
$token = $env:GITHUB_TOKEN

if (-not $token) {
    Write-Host "GitHub Personal Access Tokenが必要です。" -ForegroundColor Yellow
    Write-Host "以下の手順でトークンを取得してください:" -ForegroundColor Yellow
    Write-Host "1. https://github.com/settings/tokens にアクセス" -ForegroundColor Yellow
    Write-Host "2. 'Generate new token' をクリック" -ForegroundColor Yellow
    Write-Host "3. 'repo' スコープを選択" -ForegroundColor Yellow
    Write-Host "4. トークンをコピーして、以下のコマンドを実行:" -ForegroundColor Yellow
    Write-Host "   `$env:GITHUB_TOKEN = 'your_token_here'" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "または、以下のURLから直接Issueを作成してください:" -ForegroundColor Green
    Write-Host "https://github.com/boobeem2000/-/issues/new" -ForegroundColor Green
    exit
}

$headers = @{
    Authorization = "token $token"
    Accept = "application/vnd.github.v3+json"
}

$body = @{
    title = "集客アイデア: SNSから見込み客を見つけてDMで個別相談に流れるフロー"
    body = @"
## 概要

見込み客をSNSから見つけてきて、その人にAIで作ったDMを作って個別相談に流れるフローを作る

## 詳細

### フロー
1. **SNSから見込み客を発見**
   - Instagram、Twitter、Facebook、LinkedInなど
   - ターゲットとなるキーワードやハッシュタグで検索
   - プロフィールや投稿内容から見込み客を特定

2. **AIでDMを作成**
   - 見込み客のプロフィールや投稿内容を分析
   - AIを使って個別にカスタマイズされたDMを自動生成
   - パーソナライズされたメッセージでアプローチ

3. **個別相談に導く**
   - DMを通じて関係性を構築
   - 自然な流れで個別相談へ誘導
   - 相談からセールスへと繋げる

## 必要な機能

- [ ] SNSの見込み客検索機能
- [ ] プロフィール分析機能
- [ ] AIによるDM生成機能
- [ ] DM送信機能（手動または自動）
- [ ] 個別相談予約システムへの連携
- [ ] フロー管理ダッシュボード

## 技術スタック（検討）

- AI: ChatGPT API、Claude APIなど
- SNS連携: Instagram API、Twitter APIなど
- 自動化: Zapier、Make.comなど
- データベース: 見込み客情報の管理

## 次のステップ

1. どのSNSプラットフォームから始めるか決定
2. AIによるDM生成のプロンプト設計
3. 個別相談予約システムとの連携方法の検討
4. プライバシー・コンプライアンスの確認
"@
    labels = @("enhancement")
} | ConvertTo-Json -Depth 10

try {
    $response = Invoke-RestMethod -Uri "https://api.github.com/repos/$owner/$repo/issues" -Method Post -Headers $headers -Body $body -ContentType "application/json; charset=utf-8"
    Write-Host "Issueが作成されました!" -ForegroundColor Green
    Write-Host "URL: $($response.html_url)" -ForegroundColor Green
} catch {
    Write-Host "エラーが発生しました: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "レスポンス: $($_.Exception.Response)" -ForegroundColor Red
}

