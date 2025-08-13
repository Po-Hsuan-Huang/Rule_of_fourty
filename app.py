import dash
from dash import html, dcc, Input, Output, State
import plotly.graph_objs as go

# Initial data
initial_data = [
    ("Visa (V)",            66.77,   11.38,   570.0),
    ("TSMC (TSM)",          49.63,   38.60,   710.0),
    ("Broadcom (AVGO)",     31.76,   16.40,   660.0),
    ("Palantir (PLTR)",     26.83,   48.00,    65.0),
    ("Quad (QUAD)",          3.95,   -9.80,     0.22),
    ("Supermicro (SMCI)",    5.30,   47.00,    78.0),
    ("Axon (AXON)",          0.70,   33.00,    24.0),
    ("MercadoLibre (MELI)", 12.20,   34.00,    92.0),
    ("Credo (CRDO)",        20.39,  126.34,    18.93),
    ("Rocket Lab (RKLB)",  -43.11,   32.00,    21.45),
    ("Spotify (SPOT)",       9.68,   21.00,   133.0),
    ("Microsoft (MSFT)",    44.90,   18.00,  3966.0),
    ("Tencent (TCEHY)",     31.87,   12.90,   645.57),
    ("Joby Aviation (JOBY)", -5532.8, -9470.0, 14.86),
    ("Cloudflare (NET)",    -9.27,   27.80,    72.42),
    ("NVidia (NVDA)", 69.2 , 49.11,4340),     #4.3T


]

slope = -41 / 39  # ≈ -1.051
avg_intercept = sum(y - slope * x for _, x, y, z in initial_data) / len(initial_data)

# Create Dash app
app = dash.Dash(__name__)
server = app.server  # For deployment if needed
rule_header = html.Div([
        html.H4("📘 Rule of 40 / 40法則"),

        html.P(
            "The Rule of 40 is a metric for evaluating a company's financial health. "
            "If the intercept of Revenue Growth is greater than 40, "
            "the company is considered financially strong."
        ),
        html.P(
            "40法則衡量一家公司的成長潛力與財務韌性。"
            "任何 y 軸截距高於 40 的公司，通常同時具備強勁的營收增長與健康的獲利能力，"
            "因此被視為值得長期投資的標的。"
            "輸入您想要比較的公司代碼及指標，我們會計算該公司的 40 法則，"
            "幫助您判斷其在市場中的競爭地位。"
        ),
    ], style={"margin-bottom": "2em"})


def chapter1_content():
    return [
        html.H4("📖 第1章：後稀缺時代的黎明"),
        html.P("導論：經濟新曙光"),
        html.P(
            "數百年來，經濟學的核心問題一直圍繞著「稀缺性」——如何在有限資源與無限需求之間做出選擇。"
            "土地、勞動與資本三大生產要素，塑造了人類文明的每一次經濟飛躍。"
            "其中，勞動力的稀缺性尤其關鍵：人類的時間有限、體力有限、認知能力有限，"
            "因此每一次技術革命——從農業工具的改進、蒸汽機的誕生，到電腦的普及——"
            "都旨在讓同樣的勞動力創造更多的價值。"
            "然而，當這種根本限制消失時，我們將面對一個前所未有的世界。"
        ),
        html.P(
            "本章以一個震撼的假設為起點：人類正站在歷史上最深刻的經濟轉型門檻前——"
            "通用人工智慧（AGI）的出現。"
            "當 AGI 能以可比擬甚至超越人類的方式，執行幾乎任何認知與創造性任務時，"
            "勞動力將不再是稀缺資源，生產成本的邏輯將徹底顛覆。"
        ),

        html.H5("舊世界：稀缺、勞動與價值"),
        html.P(
            "傳統經濟的邏輯可以用三個核心概念來理解："
        ),
        html.Ul([
            html.Li("資源（Resources）：土地、勞動、資本是生產的基礎。對於大多數時期的人類社會，勞動力是最稀缺且最昂貴的資源。"),
            html.Li("生產力（Productivity）：衡量資源轉化為產品或服務的效率。歷史上，生產力的提升幾乎總是透過輔助工具與技術來放大勞動力的產出。"),
            html.Li("價值（Value）：價值的形成與投入的勞動成本密切相關，從設計者、工匠，到運輸與銷售的每一環節，都蘊含著人力成本。")
        ]),
        html.P(
            "想像建造一棟房子：土地與材料固然重要，但最大的成本來自於人力——建築師的設計、木工與水電工的施工、工程監理的管理。"
            "但若這些角色全由 AGI 以零疲勞、零休息的方式完成，且僅需支付計算與能源成本，那麼價值的衡量方式將徹底改變。"
        ),

        html.H5("AGI 革命：當勞動變得充裕"),
        html.P(
            "今天的人工智慧（窄 AI）已能在特定領域超越人類，例如圍棋對弈、語音識別、影像分類。"
            "然而 AGI 的目標並非單點突破，而是具備與人類相似的通用認知與學習能力，"
            "能夠跨領域整合知識、理解複雜問題、做出策略決策，甚至創造新知。"
        ),
        html.P(
            "這意味著，AGI 將不僅取代重複性勞動，還將深入科學研究、產品設計、文化創作與政策規劃等高度智力密集的領域。"
            "一旦勞動力變得「可無限複製且幾乎免費」，傳統經濟中最核心的稀缺性將瞬間消失。"
        ),

        html.H5("新經濟學：跨越勞動障礙"),
        html.P(
            "當勞動力成本不再構成生產瓶頸時，新的稀缺性將轉移到其他領域："
        ),
        html.Ul([
            html.Li("能源（Energy）：為全球 AGI 與自動化系統供電需要巨大且穩定的能源輸入，能源的成本與清潔度將決定經濟競爭力。"),
            html.Li("原材料（Raw Materials）：再強大的智慧系統也需要物質基礎，如鋼鐵、晶片、稀土，這些實體資源的開採與加工將成為新的戰略制高點。"),
            html.Li("計算資源（Computational Resources）：資料中心的運算力、儲存容量與網路頻寬將直接影響生產與創新的上限。")
        ]),
        html.P(
            "在這個新世界中，一國的繁榮不再取決於人口的就業率，而是能源網絡的韌性、資源獲取的能力、以及計算基礎設施的規模與效率。"
        ),

        html.H5("結論：必須重新提出的問題"),
        html.P(
            "當 AGI 能夠滿足人類所有物質與大部分精神需求時，經濟學的核心將從「如何賺錢維持生計」轉向「如何分配與使用無限的生產力」。"
            "這將引發一系列前所未有的問題："
            "我們如何確保財富的公平分配？"
            "人類在價值創造中的角色是什麼？"
            "「工作」與「休閒」的界線又該如何重新界定？"
        ),
        html.P(
            "20 世紀的經濟學關注如何透過就業來克服個人的匱乏；"
            "21 世紀及以後的經濟學將關注如何建立能在豐饒時代持續繁榮的人類社會。"
            "歡迎來到經濟學 101 —— 未來已然展開。"
        )  
    ]

def chapter2_content():
    return [
        html.H4("📖 第2章：能源・材料・計算——新的三大稀缺"),
        html.P(
            "在後稀缺框架下，限制經濟增長的不再是人力，而是能源、材料與計算三者的耦合瓶頸。"
            "本章從技術—制度—地緣政治三個維度，解析這三大稀缺如何構成新的宏觀約束。"
        ),
        html.H5("一、能源：從成本到體系韌性"),
        html.P(
            "能源不僅是成本，更是「可用性 × 穩定性 × 潔淨度」的向量。當智能與自動化滲透實體經濟，"
            "負載曲線更尖銳，尖峰供給與儲能調度成為核心工程問題。"
            "國家競爭力將取決於低邊際成本能源與高彈性電網的組合。"
        ),
        html.H5("二、材料：物理世界的基礎摩擦"),
        html.P(
            "原材料的稀缺源自地質分布、提煉難度與地緣風險。即便設計與軟體可瞬間複製，"
            "物質世界仍需時間與物流；循環材料學與近源製造將成為供應鏈韌性的關鍵槓桿。"
        ),
        html.H5("三、計算：算力結構與演算法效率"),
        html.P(
            "算力不僅是 GPU 數量，更涉及記憶體頻寬、互連拓撲、資料在地性與軟硬協同。"
            "在相同硬體條件下，演算法效率可帶來數量級的能耗與成本差異，"
            "成為企業邊際競爭力的隱形分水嶺。"
        ),
        html.H5("結語：三者協同的政策與治理"),
        html.P(
            "能源、材料與計算互為邊界條件：能源擴張賦能算力與材料提煉；"
            "材料創新反過來降低能源—算力單位成本；計算優化又提升能源與材料配置效率。"
            "能在三者間達成跨域協同與長期主權保障的經濟體，將在後稀缺時代拔得頭籌。"
        ),
    ]
def chapter3_content():
    return [
        html.H4("📖 第3章：分配、所有權與激勵——後稀缺時代的制度設計"),
        html.P(
            "前兩章指出：當可複製的智能使勞動不再稀缺，經濟的瓶頸轉向能源、材料與計算。"
            "然而，生產力的外擴並不自動等於福祉的提升；制度如何界定「誰擁有什麼、誰獲得什麼、"
            "以及人們為何而努力」，將決定後稀缺時代的分配結構與文明走向。"
        ),

        html.H5("一、分配機制：從『所得』到『權益配給』"),
        html.P(
            "當邊際生產主要由機器完成，傳統以工資為核心的分配機制將失去錨點。"
            "分配邏輯需從『所得』轉向對稀缺要素與公共產出的『權益配給』。"
        ),
        html.Ul([
            html.Li("普惠分紅（Social Dividend）：以主權基金或公共資產（如能源、算力、頻譜、土地收益）為底，向全體公民按人頭發放分紅。"),
            html.Li("資料與模型紅利（Data / Model Dividend）：個人與社群對資料、標註與情境貢獻有持續分享機制，避免『零價格—零補償』的剝奪。"),
            html.Li("算力與能源配額（Compute / Energy Credits）：對稀缺要素發放可交易配額，既保障基本使用權，又讓市場在邊際上配置效率。"),
            html.Li("公共品回購（Retroactive Public Goods Funding）：對事後證明高社會價值的科研與開源項目給予溯及性的財務回報，形成長期激勵。"),
        ]),

        html.H5("二、所有權：從排他到共益的版圖重繪"),
        html.P(
            "在可複製的數位世界，強排他性的所有權容易抑制外部性與疊代創新；"
            "而完全無邊界的共享又可能產生『公地悲劇』。"
            "後稀缺治理需在兩者間找到可演化的中間態。"
        ),
        html.Ul([
            html.Li("模組化權利束（Bundle of Rights）：將『使用、收益、改作、分發』拆分，針對模型權重、資料語料、提示工程各自制定細分權利。"),
            html.Li("共享—商用雙軌（Dual Licensing）：基礎模型與資料集以開源、非商用或條款限制釋出，商業化則採取合理授權費與分潤。"),
            html.Li("社群治理與憲章（Community Charter）：由多方節點共同維護模型與資料治理準則，透過投票與審計維持邊界與品質。"),
            html.Li("主權算力與資料托管（Sovereign Compute/Data）：在跨國供應鏈風險下，關鍵算力與資料採去中心而可審計的主權托管架構。"),
        ]),

        html.H5("三、激勵設計：讓創新與公益同向"),
        html.P(
            "當『工作＝收入』鬆動，激勵便需回到目的本身：追求真理、創造美、照護他人、保護環境、"
            "推進制度品質。機制設計的核心，是讓個體追求自利時也能擴大公共價值。"
        ),
        html.Ul([
            html.Li("獎金制與挑戰賽（Prize Mechanisms）：以明確目標與可驗證指標來引導研發，避免『補助—指標扭曲』。"),
            html.Li("二次方資助（Quadratic Funding）：以小額多數偏好加權，鼓勵分散式創新與社群優先議題。"),
            html.Li("影子價格與外部性稅（Pigouvian Tools）：對碳、資安風險、對齊失誤等外部性賦予價格，以市場方式內生化治理。"),
            html.Li("可驗證憑證（Verifiable Credentials）：把貢獻與聲譽轉為可攜帶、可審核的資產，降低協作中的逆向選擇與道德風險。"),
        ]),

        html.H5("四、貨幣與財政：在豐饒中校準價格訊號"),
        html.P(
            "後稀缺並不意味價格消失；價格應從反映『人力成本』轉向反映『實體瓶頸與風險溢價』。"
            "宏觀政策要務，是穩定關鍵稀缺要素的投資節奏與期望。"
        ),
        html.Ul([
            html.Li("抗波動的投資規則：對電網、儲能、關鍵材料與算力的長週期保底機制，平滑景氣循環與技術迭代的不確定。"),
            html.Li("通縮—通膨的結構疊加：可複製品長期通縮，實體稀缺品可能通膨；指標體系需區隔『數位價格籃』與『實體價格籃』。"),
            html.Li("主權基金與代際公平：把資源收益轉為可永續分配的金融資產，避免一次性消費與代際不公。"),
        ]),

        html.H5("五、風險與護欄：把失靈鎖在系統外"),
        html.P(
            "系統風險來源包括：模型對齊失敗、濫用與擴散、供應鏈單點脆弱、以及『黑箱決策』。"
            "治理需要可觀測、可追溯、可終止的技術與法制組合。"
        ),
        html.Ul([
            html.Li("分級使用與沙盒：依能力與風險分級准入；高風險應用須在審計沙盒中運行並留存日誌。"),
            html.Li("計算執照與安全基線：大型訓練需申報資料來源、能耗與評測結果，達到最低安全基線方可部署。"),
            html.Li("可追責的代理鏈：對自治代理的行為建立簽名與可驗證溯源，落實『誰部署、誰負責』。"),
            html.Li("失效安全（Fail-safe）與斷路器：在異常輸出與行為偵測到位時，能快速降級與隔離。"),
        ]),

        html.H5("六、過渡路徑：從當下走向後稀缺"),
        html.P(
            "制度的可行性取決於過渡成本。政策設計需避免『一刀切』，以序列化、可回退的方式推進。"
        ),
        html.Ul([
            html.Li("雙迴路策略：在現行工資體系上疊加權益配給試點，逐步提高公共分紅與配額比重。"),
            html.Li("技能轉換與身份保障：提供長年限再訓練、職涯轉軌保險與創業支持，降低轉型摩擦。"),
            html.Li("地方試點—聯邦擴散：先在能源充裕、數據治理成熟的地區試行，形成標準後再全域推廣。"),
        ]),

        html.H5("結語：把文明目標內嵌進經濟機制"),
        html.P(
            "後稀缺不是『沒有選擇的烏托邦』，而是『需要更好選擇的現實』。"
            "分配、所有權與激勵的設計，必須把文明目標——真理、善意、自由與美——"
            "內嵌為可運行、可審計、可演化的制度程式。"
            "當制度能讓個體的追求自然匯聚為公共價值，後稀缺才可能成為後匱乏的人類社會。"
        ),
    ]

app.layout = html.Div([
    html.H1("Rule of 40"),

    rule_header,

    # Controls: height slider + label + next chapter button
    html.Div([
        html.Div([
            html.Label("閱讀框高度（px）", style={"fontWeight": "600"}),
            dcc.Slider(
                id="height-slider",
                min=300, max=1000, step=50, value=600,
                marks={300: "300", 600: "600", 900: "900", 1000: "1000"},
                tooltip={"placement": "bottom", "always_visible": False},
            ),
            html.Div(id="height-label", style={"marginTop": "0.5rem", "fontSize": "0.9rem", "opacity": 0.8}),
        ], style={"flex": "1"}),

    html.Div([
        html.Button("下一章 Next chapter →", id="next-btn",
                    style={
                        "padding": "10px 16px",
                        "borderRadius": "10px",
                        "border": "1px solid #ddd",
                        "cursor": "pointer",
                        "background": "white",
                        "boxShadow": "0 1px 4px rgba(0,0,0,0.08)",
                        "fontWeight": 600
                    })
        ], style={"display": "flex", "alignItems": "flex-end", "paddingLeft": "1rem"})
    ], style={"display": "flex", "gap": "1.5rem", "marginBottom": "1rem"}),

    dcc.Store(id="chapter-index", data=0),

    # Scrollable chapter box (height controlled by slider)
    html.Div(
        id="chapter-box",
        children=[
            html.Div(id="chapter-content", children=chapter1_content())
        ],
        style={
            'width': '90%',
            'float': 'left',
            "padding": "1em",
            "border": "1px solid #ccc",
            "borderRadius": "10px",
            "backgroundColor": "#222222",
            "maxHeight": "600px",   # will be updated by slider
            "overflowY": "auto"     # scroller
        }),
    

    
    html.Div([
        html.Label("Company Ticker Label:   "),
        dcc.Input(id='input-label', type='text', placeholder='e.g. NVDA'),
        html.Button('Add Company', id='submit-button', n_clicks=0),
        html.H1(""),
        html.Label("Adjusted Operating Margin (%):   "),
        dcc.Input(id='input-margin', type='number', step=0.01),
        html.H1(""),
        html.Label("YoY Revenue Growth (%):   "),
        dcc.Input(id='input-growth', type='number', step=0.01),
        html.H1(""),
        html.Label("Market Cap (Billion):  "),
        dcc.Input(id='input-market-cap', type='number', step=0.01)
    ], style={'width': '30%',
        'float': 'left',
        'margin': '20px',
        'padding': '20px',
        'fontSize': '16px'}),

    html.Div([
        dcc.Store(id='company-data', data=initial_data),
        dcc.Graph(id='scatter-plot')
    ], style={
        'width': '68%',
        'float': 'left'
    })

], style={ "margin": "0 auto", "padding": "1rem"})

@app.callback(
    Output("chapter-box", "style"),
    Output("height-label", "children"),
    Input("height-slider", "value"),
    State("chapter-box", "style"),
)
def update_box_height(px, style):
    """Adjust the scroll-box height and show current value."""
    style = dict(style or {})
    style["maxHeight"] = f"{px}px"
    style["overflowY"] = "auto"  # force scroller when overflow
    return style, f"目前高度：{px}px"

@app.callback(
    Output("chapter-content", "children"),
    Output("chapter-index", "data"),
    Input("next-btn", "n_clicks"),
    State("chapter-index", "data"),
)

def next_chapter(n, idx):
    """Cycle chapters when button is clicked."""
    idx = (idx or 0)
    if not n:
        # initial render
        return chapter1_content(), idx
    new_idx = (idx + 1) % 3
    if new_idx == 0:
        return chapter1_content(), new_idx
    elif new_idx == 1:
        return chapter2_content(), new_idx
    elif new_idx == 2:
        return chapter3_content(), new_idx
    else :
        return chapter1_content(), new_idx

@app.callback(
    Output('company-data', 'data'),
    Input('submit-button', 'n_clicks'),
    State('input-label', 'value'),
    State('input-margin', 'value'),
    State('input-growth', 'value'),
    State('input-market-cap', 'value'),
    State('company-data', 'data'),
)

def update_data(n_clicks, label, margin, growth, cap, data):
    if n_clicks > 0 and label and margin is not None and growth is not None:
        data.append((label, margin, growth, cap))
    return data

@app.callback(
    Output('scatter-plot', 'figure'),
    Input('company-data', 'data')
)

def update_plot(data):
    labels, margins, growths, caps = zip(*data)
    intercept_line = 40 #

    # Regression line
    x_line = list(range(0, int(max(margins)) + 5))
    y_line = [slope * x + intercept_line for x in x_line]

    intercepts = [y - slope * x for x, y in zip(margins, growths)]
    hover_texts = [
        f"{label}<br>Margin: {x:.2f}%<br>Growth: {y:.2f}%<br>Market Cap: {c:.2f}B<br>Intercept: {b:.2f}"
        for label, x, y, c, b in zip(labels, margins, growths, caps, intercepts)
    ]
    scatter = go.Scatter(
        x=margins,
        y=growths,
        mode='markers+text',
        text=labels,
        hovertext=hover_texts,
        textposition='top center',
        marker=dict(
            size=caps,
            sizemode='area',
            sizeref=2.*max(caps)/(80.**2),  # adjust for visual scaling
            sizemin=5,
            color='cyan'
        ), # Changed marker color for dark mode visibility
        name='Companies'
    )

    line = go.Scatter(
        x=x_line,
        y=y_line,
        mode='lines',
        name='Rule of 40 Frontier',
        line=dict(color='red', dash='dash')
    )

    layout = go.Layout(
        xaxis=dict(
            title='Adjusted Operating Margin (%)',
            range = [0,75],
            dtick=10,
            gridcolor='#444444', # Darker grid lines
            zerolinecolor='#666666',
            tickfont=dict(color='#f0f0f0'), # Light tick labels
            title_font=dict(color='#f0f0f0') # Light title font
        ),
        yaxis=dict(
            title='YoY Revenue Growth (%)',
            range=[0, 145],
            dtick=10,
            gridcolor='#444444', # Darker grid lines
            zerolinecolor='#666666',
            tickfont=dict(color='#f0f0f0'), # Light tick labels
            title_font=dict(color='#f0f0f0'), # Light title font
        ),
        showlegend=True,
        width=1600,
        height=600,

        plot_bgcolor='#333333', # Dark background for the plot area
        paper_bgcolor='#222222', # Dark background for the entire figure
        font=dict(color='#f0f0f0') # Default font color for the graph
    
    )




    return go.Figure(data=[scatter, line], layout=layout)





if __name__ == '__main__':
    app.run(debug=True)
