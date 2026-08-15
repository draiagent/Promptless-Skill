# 範例：企業市場研究 Promptless Agent

## 使用情境

主管只提出：

> 「幫我比較三個主要競爭品牌，提出下季策略。」

不要求主管先寫 Role / Context / Chain / Output Prompt。

## Skill 層

- 市場搜尋 Skill
- 競品比較 Skill
- 數據分析 Skill
- 策略摘要 Skill
- 簡報 Skill

## VAD Agent

### GOAL
完成可供管理層決策的競品分析與策略建議。

### ROLE
市場策略 Agent；不自行發布對外聲明、不修改正式財務資料。

### SKILLS
Research / Compare / Analyze / Strategy / Presentation

### TOOLS
Search、Files、Spreadsheet、Presentation Tool（依平台可用能力）

### KNOWLEDGE
公司策略文件、產品資料、公開市場資料。

### WORKFLOW
搜尋 → 來源驗證 → 競品矩陣 → 差距分析 → 策略選項 → QA → 簡報。

### DECISION
- AUTO：選擇可信公開來源。
- ASK：公司內部策略互相衝突。
- ESCALATE：需要法律／財務專業判斷。
- STOP：缺乏足夠可信資料卻要求確定結論。

### SUB-AGENTS
可拆市場研究 Agent、財務 Agent、簡報 Agent。

### MCP / A2A
有 CRM / ERP / 搜尋服務時可用 MCP；多代理間可用 A2A 協作。

### QA
來源日期、資料一致性、假設標示、策略與證據對應、主管 Human Review。
