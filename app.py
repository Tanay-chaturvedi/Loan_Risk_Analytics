import os
from io import BytesIO
import joblib
import pandas as pd
import streamlit as st
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

st.set_page_config(page_title='LoanLens AI', page_icon='🏦', layout='wide')
st.markdown('''<style>
.stApp{background:#eef8ff}.block-container{max-width:1200px;padding-top:5.2rem!important;padding-bottom:3rem}.stButton{overflow:visible!important}header[data-testid='stHeader']{background:rgba(238,248,255,.96)!important}.stButton>button{overflow:visible!important}.brand{font-size:25px;font-weight:800;color:#0f4c81}.brand span,.blue{color:#2386c8}.hero{font-size:56px;line-height:1.05;font-weight:850;color:#12324a}.hero span{color:#2386c8}.sub{color:#61798a;font-size:17px;line-height:1.6}.section{font-size:31px;font-weight:800;color:#12324a;margin-top:28px}.card,.metric,.factor{background:linear-gradient(145deg,#ffffff,#f4faff);border:1px solid #d8eaf5;border-radius:18px;padding:22px;box-shadow:5px 6px 14px rgba(30,90,120,.07),-4px -4px 10px rgba(255,255,255,.9);transition:all .25s ease}.card:hover,.metric:hover,.factor:hover{transform:translateY(-4px);box-shadow:7px 11px 22px rgba(30,90,120,.12),-4px -4px 12px rgba(255,255,255,.95)}.metric{text-align:center}.num{font-size:29px;font-weight:800;color:#12679b}.label,.muted{color:#718693;font-size:13px}.approved{background:linear-gradient(145deg,#effdf6,#e5f8ee);border:1px solid #a9e4c8;border-radius:20px;padding:28px;box-shadow:5px 8px 20px rgba(35,130,90,.08)}.rejected{background:linear-gradient(145deg,#fff7f7,#fff0f0);border:1px solid #f1b7b7;border-radius:20px;padding:28px;box-shadow:5px 8px 20px rgba(160,60,60,.08)}.result{font-size:34px;font-weight:850;color:#17394d}.prob{font-size:46px;font-weight:850;color:#12679b}.footer{text-align:center;color:#7a8d98;font-size:13px;padding:30px}div.stButton>button,div[data-testid='stDownloadButton'] button{border-radius:11px;font-weight:700;min-height:44px;height:44px;line-height:1.2;padding:8px 16px;margin:0;box-shadow:0 4px 8px rgba(35,100,140,.12);transition:all .2s ease}div.stButton>button:hover,div[data-testid='stDownloadButton'] button:hover{transform:translateY(-2px);box-shadow:0 7px 14px rgba(35,100,140,.18)}

.perf-card{background:linear-gradient(145deg,#ffffff,#f5faff);border:1px solid #d6e8f3;border-radius:20px;padding:24px;box-shadow:6px 8px 20px rgba(30,90,120,.07),-4px -4px 12px rgba(255,255,255,.9);margin-bottom:18px}
.perf-card-head{display:flex;justify-content:space-between;align-items:center;gap:15px;margin-bottom:18px}
.perf-title{font-size:21px;font-weight:850;color:#17394d}.perf-subtitle{font-size:13px;color:#7a8d98;margin-top:4px}
.model-pill,.importance-badge{background:#e7f4fd;color:#12679b;border:1px solid #c7e5f5;border-radius:999px;padding:7px 13px;font-size:12px;font-weight:800;white-space:nowrap}
.comparison-table-wrap{overflow:hidden;border:1px solid #dbeaf3;border-radius:14px}.comparison-table{width:100%;border-collapse:collapse;font-size:14px}.comparison-table th{background:#12679b;color:white;text-align:left;padding:14px 16px;font-weight:800}.comparison-table td{padding:14px 16px;border-bottom:1px solid #e7f0f5;color:#536b79;background:white}.comparison-table tr:nth-child(even) td{background:#f8fcff}.comparison-table tr:last-child td{border-bottom:none}.comparison-table .metric-name{font-weight:800;color:#17394d}.rf-value{display:inline-block;background:#e9f7ff;color:#12679b;border:1px solid #c9e8f6;border-radius:8px;padding:5px 9px;font-weight:850}.table-note{font-size:12px;color:#8497a2;margin-top:10px}
.legend-row{display:flex;gap:22px;justify-content:flex-end;color:#687f8d;font-size:12px;margin-bottom:16px}.legend-dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;background:#9fb6c4}.rf-dot{background:#2386c8}.perf-bar-row{padding:15px 0;border-top:1px solid #edf3f7}.perf-bar-row:first-of-type{border-top:none}.perf-bar-label{font-weight:800;color:#17394d;font-size:14px;margin-bottom:9px}.bar-line{display:grid;grid-template-columns:28px 1fr 58px;align-items:center;gap:8px;margin:6px 0}.bar-model{font-size:11px;font-weight:800;color:#7a8d98}.bar-track{height:9px;background:#eaf2f6;border-radius:99px;overflow:hidden}.bar-fill{height:100%;border-radius:99px}.lr-fill{background:#9fb6c4}.rf-fill{background:#2386c8}.bar-number{font-size:12px;font-weight:800;color:#506b7a;text-align:right}
.cm-card{background:linear-gradient(145deg,#ffffff,#f5faff);border:1px solid #d6e8f3;border-radius:20px;padding:22px;box-shadow:6px 8px 20px rgba(30,90,120,.07),-4px -4px 12px rgba(255,255,255,.9)}.cm-title{font-size:19px;font-weight:850;color:#17394d}.cm-subtitle{font-size:12px;color:#8497a2;margin:4px 0 17px}.cm-grid{display:grid;grid-template-columns:82px 1fr 1fr;gap:6px}.cm-label{display:flex;align-items:center;justify-content:center;text-align:center;font-size:11px;font-weight:800;color:#728793;padding:7px}.cm-label.side{justify-content:flex-start}.cm-cell{min-height:90px;border-radius:12px;padding:12px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;border:1px solid #dceaf2}.cm-cell small{font-size:10px;color:#718693;margin-bottom:5px}.cm-cell strong{font-size:25px;color:#17394d}.cm-cell.tn{background:#edf9f3;border-color:#c5ead6}.cm-cell.tp{background:#e8f6fd;border-color:#c4e4f3}.cm-cell.fp{background:#fff5ea;border-color:#f2d7b4}.cm-cell.fn{background:#fff1f1;border-color:#efc5c5}
.fi-row{display:grid;grid-template-columns:155px 1fr 65px;align-items:center;gap:14px;padding:13px 0;border-bottom:1px solid #edf3f7}.fi-row:last-of-type{border-bottom:none}.fi-name{font-size:13px;font-weight:750;color:#526d7b}.fi-track{height:13px;background:#e9f2f6;border-radius:99px;overflow:hidden}.fi-fill{height:100%;background:linear-gradient(90deg,#2386c8,#5ba9d7);border-radius:99px}.fi-value{font-size:13px;font-weight:850;color:#12679b;text-align:right}
@media(max-width:700px){.perf-card-head{align-items:flex-start;flex-direction:column}.fi-row{grid-template-columns:120px 1fr 55px}.cm-grid{grid-template-columns:65px 1fr 1fr}.legend-row{justify-content:flex-start}.comparison-table{font-size:12px}.comparison-table th,.comparison-table td{padding:11px 9px}}
</style>''', unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page='home'
if 'last' not in st.session_state: st.session_state.last=None

@st.cache_resource
def load_model():
    p=os.path.join('models','loan_approval_random_forest.pkl')
    if not os.path.exists(p): st.error('Model not found: models/loan_approval_random_forest.pkl'); st.stop()
    return joblib.load(p)
model=load_model()

def explain(r):
    x=[]; c=int(r.cibil_score); ratio=r.loan_amount/r.income_annum if r.income_annum else 999
    if c>=750:x.append(f'CIBIL score of {c} is high and is the strongest feature in this project model.')
    elif c>=650:x.append(f'CIBIL score of {c} is moderate-to-good and is an important model input.')
    elif c>=550:x.append(f'CIBIL score of {c} is relatively low and can reduce the predicted approval probability.')
    else:x.append(f'CIBIL score of {c} is low and can strongly affect the model prediction.')
    x.append(f"The selected loan term is {int(r.loan_term)} years.")
    if ratio<=3:x.append('The requested loan amount is relatively low compared with annual income.')
    elif ratio<=5:x.append('The requested loan amount is moderate relative to annual income.')
    else:x.append('The requested loan amount is high relative to annual income.')
    x.append('The final prediction is generated from the combined pattern of all input features, not a single rule.')
    return x

def pdf(a):
    b=BytesIO(); doc=SimpleDocTemplate(b,pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=18*mm,bottomMargin=18*mm)
    s=getSampleStyleSheet(); title=ParagraphStyle('t',parent=s['Title'],fontSize=24,alignment=TA_CENTER,textColor=colors.HexColor('#12324a')); h=ParagraphStyle('h',parent=s['Heading2'],fontSize=15,textColor=colors.HexColor('#12679b')); n=ParagraphStyle('n',parent=s['Normal'],fontSize=10,leading=15,textColor=colors.HexColor('#334e5e'))
    story=[Paragraph('LoanLens AI',title),Paragraph('Loan Approval Assessment Report',ParagraphStyle('sub',parent=n,alignment=TA_CENTER)),Spacer(1,15)]
    story += [Table([['Prediction',a['status']],['Approval Probability',f"{a['probability']:.2f}%"]],colWidths=[65*mm,90*mm],style=TableStyle([('BACKGROUND',(0,0),(0,-1),colors.HexColor('#eef8ff')),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#d8eaf5')),('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)])),Spacer(1,12),Paragraph('Applicant Details',h)]
    rows=[['Field','Value'],['Dependents',str(a['no_of_dependents'])],['Education',a['education']],['Self Employed',a['self_employed']],['Annual Income',f"₹{a['income_annum']:,.0f}"],['Loan Amount',f"₹{a['loan_amount']:,.0f}"],['Loan Term',f"{a['loan_term']} years"],['CIBIL Score',str(a['cibil_score'])],['Residential Assets',f"₹{a['residential_assets_value']:,.0f}"],['Commercial Assets',f"₹{a['commercial_assets_value']:,.0f}"],['Luxury Assets',f"₹{a['luxury_assets_value']:,.0f}"],['Bank Assets',f"₹{a['bank_asset_value']:,.0f}"]]
    story += [Table(rows,colWidths=[65*mm,90*mm],repeatRows=1,style=TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#12679b')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#d8eaf5')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f8fcff')]),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)])),Spacer(1,12),Paragraph('Prediction Explanation',h)]
    story += [Paragraph('• '+z,n) for z in a['explanation']]+[Spacer(1,8),Paragraph('Model Information',h),Paragraph('Prediction generated using the deployed Random Forest classifier. This is a decision-support prototype and does not replace regulatory checks, bank policies, or human review.',n)]
    doc.build(story); return b.getvalue()

def nav():
    c1,c2=st.columns([.25,.75]);
    with c1:
        if st.button('← Home',use_container_width=True): st.session_state.page='home'; st.rerun()
    with c2: st.markdown('<div style="text-align:right" class="brand">LoanLens <span>AI</span></div>',unsafe_allow_html=True)

def home():
    st.markdown('<div class="brand">LoanLens <span>AI</span></div>',unsafe_allow_html=True); st.write('')
    a,b=st.columns([1.15,.85])
    with a:
        st.markdown('<div class="hero">Understand your<br><span>loan approval</span> outlook.</div>',unsafe_allow_html=True)
        st.markdown('<p class="sub">LoanLens AI uses a trained Random Forest model to estimate loan approval outcomes from applicant and financial information.</p>',unsafe_allow_html=True)
        x,y=st.columns(2)
        with x:
            if st.button('Start Assessment →',type='primary',use_container_width=True):st.session_state.page='assessment';st.rerun()
        with y:
            if st.button('View Model Performance',use_container_width=True):st.session_state.page='performance';st.rerun()
    with b:
        st.markdown('''<div class="card"><div class="muted">SAMPLE ASSESSMENT</div><h1 style="color:#12324a">97.5% <span style="font-size:13px;background:#eafaf3;color:#168452;padding:7px 12px;border-radius:20px">APPROVED</span></h1><div class="factor">CIBIL 750</div><div class="factor">Annual Income ₹80 L</div><div class="factor">Loan Amount ₹2 Cr</div></div>''',unsafe_allow_html=True)
    st.markdown('<div class="section">Model at a glance</div>',unsafe_allow_html=True); st.write('')
    for c,(n,l) in zip(st.columns(4),[('98.13%','Test Accuracy'),('99.86%','ROC-AUC'),('4,269','Applications'),('11','Input Features')]):
        c.markdown(f'<div class="metric"><div class="num">{n}</div><div class="label">{l}</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="section">How it works</div>',unsafe_allow_html=True); st.write('')
    steps=[('01','Enter applicant details'),('02','Preprocess inputs'),('03','Run Random Forest'),('04','Review assessment')]
    for c,(n,t) in zip(st.columns(4),steps):
        c.markdown(f'<div class="card"><div class="blue"><b>{n}</b></div><h4 style="color:#17394d">{t}</h4><div class="muted">Complete one step of the end-to-end ML pipeline.</div></div>',unsafe_allow_html=True)

    st.markdown('<div class="section">Top model factors</div>',unsafe_allow_html=True)
    for c,(n,v) in zip(st.columns(5),[('CIBIL Score','Highest'),('Loan Term','6.15%'),('Loan Amount','3.09%'),('Annual Income','1.95%'),('Luxury Assets','1.95%')]):
        c.markdown(f'<div class="factor"><div class="muted">{n}</div><div class="num">{v}</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="card" style="margin-top:12px;"><div style="color:#5d7482;line-height:1.6;font-size:14px;"><b style="color:#17394d;">CIBIL Score is the dominant feature</b> in the trained Random Forest model. Feature importance indicates model reliance, not causation.</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="footer">LoanLens AI • Machine Learning-II Project • Decision-support prototype</div>',unsafe_allow_html=True)

def assessment():
    nav(); st.markdown('<div class="section">Loan Assessment</div><div class="sub">Enter applicant information to generate a model-based prediction.</div>',unsafe_allow_html=True)
    with st.form('loan'):
        c1,c2,c3=st.columns(3)
        dep=c1.number_input('Number of Dependents',0,20,2)
        edu=c2.selectbox('Education',['Graduate','Not Graduate'])
        emp=c3.selectbox('Self Employed',['No','Yes'])
        c1,c2=st.columns(2)
        inc=c1.number_input('Annual Income (₹)',0,100000000,8000000,100000)
        loan=c1.number_input('Loan Amount (₹)',0,100000000,20000000,100000)
        term=c1.number_input('Loan Term (Years)',1,50,10)
        cibil=c1.number_input('CIBIL Score',300,900,750)
        res=c2.number_input('Residential Assets Value (₹)',0,100000000,10000000,100000)
        com=c2.number_input('Commercial Assets Value (₹)',0,100000000,5000000,100000)
        lux=c2.number_input('Luxury Assets Value (₹)',0,100000000,15000000,100000)
        bank=c2.number_input('Bank Asset Value (₹)',0,100000000,7000000,100000)
        go=st.form_submit_button('Generate Loan Assessment →',type='primary',use_container_width=True)
    if go:
        d=pd.DataFrame({'no_of_dependents':[dep],'education':[edu],'self_employed':[emp],'income_annum':[inc],'loan_amount':[loan],'loan_term':[term],'cibil_score':[cibil],'residential_assets_value':[res],'commercial_assets_value':[com],'luxury_assets_value':[lux],'bank_asset_value':[bank]})
        pred=int(model.predict(d)[0]); p=float(model.predict_proba(d)[0][1]*100); status='Approved' if pred==1 else 'Rejected'
        st.session_state.last={**d.iloc[0].to_dict(),'status':status,'probability':p,'explanation':explain(d.iloc[0])}
    a=st.session_state.last
    if a:
        cls='approved' if a['status']=='Approved' else 'rejected'
        st.markdown(f'<div class="{cls}"><div class="result">{a["status"]}</div><div class="muted">Model-based loan approval classification</div><div class="prob">{a["probability"]:.2f}%</div><div class="muted">Approval probability</div></div>',unsafe_allow_html=True)
        c1,c2=st.columns([1.2,.8])
        with c1:
            st.markdown('<div class="card"><h3 style="color:#17394d">Why the model reached this result</h3>',unsafe_allow_html=True)
            for z in a['explanation']: st.markdown('• '+z)
            st.markdown('</div>',unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="card"><h3 style="color:#17394d">Key Inputs</h3><p class="muted">CIBIL</p><h2 class="blue">{a["cibil_score"]}</h2><p class="muted">Loan Term</p><h2 class="blue">{a["loan_term"]} years</h2><p class="muted">Loan Amount</p><h3 style="color:#12679b">₹{a["loan_amount"]:,.0f}</h3></div>',unsafe_allow_html=True)
        st.download_button('⬇ Download Assessment PDF',pdf(a),'LoanLens_AI_Assessment.pdf','application/pdf',use_container_width=True)

def performance():
    nav()
    st.markdown('<div class="section">Model Performance</div><div class="sub">A clean comparison of model quality, classification errors, and the factors used by the deployed Random Forest.</div>', unsafe_allow_html=True)
    st.write('')

    comparison=[('Accuracy',91.45,98.13),('Precision',92.10,98.49),('Recall',94.35,98.49),('F1-Score',93.21,98.49),('ROC-AUC',97.26,99.86)]
    rows_html=''
    for metric,lr,rf in comparison:
        rows_html += f'<tr><td class="metric-name">{metric}</td><td>{lr:.2f}%</td><td><span class="rf-value">{rf:.2f}%</span></td></tr>'

    st.markdown(f'''
    <div class="perf-card">
      <div class="perf-card-head"><div><div class="perf-title">Model comparison</div><div class="perf-subtitle">Evaluation on the project test set</div></div><div class="model-pill">Random Forest</div></div>
      <div class="comparison-table-wrap"><table class="comparison-table"><thead><tr><th>Metric</th><th>Logistic Regression</th><th>Random Forest</th></tr></thead><tbody>{rows_html}</tbody></table></div>
      <div class="table-note">Higher values indicate stronger performance for all metrics shown.</div>
    </div>
    ''',unsafe_allow_html=True)

    kpis=[('98.13%','Random Forest Accuracy','Test set'),('99.86%','Random Forest ROC-AUC','Test set'),('98.49%','Random Forest F1-Score','Test set'),('4,269','Dataset Applications','Total rows')]
    for col,(value,title,note) in zip(st.columns(4),kpis):
        col.markdown(f'<div class="metric"><div class="num">{value}</div><div class="label" style="font-size:14px;margin-top:4px;">{title}</div><div style="color:#9aabb5;font-size:11px;margin-top:5px;">{note}</div></div>',unsafe_allow_html=True)

    st.markdown('<div class="section">Performance by metric</div><div class="sub">The same test-set metrics shown above, presented visually for quick comparison.</div>',unsafe_allow_html=True)
    st.write('')
    bars_html=''
    for metric,lr,rf in comparison:
        bars_html += f'<div class="perf-bar-row"><div class="perf-bar-label">{metric}</div><div class="bar-line"><span class="bar-model">LR</span><div class="bar-track"><div class="bar-fill lr-fill" style="width:{lr}%;"></div></div><span class="bar-number">{lr:.2f}%</span></div><div class="bar-line"><span class="bar-model">RF</span><div class="bar-track"><div class="bar-fill rf-fill" style="width:{rf}%;"></div></div><span class="bar-number">{rf:.2f}%</span></div></div>'
    st.markdown(f'<div class="perf-card"><div class="legend-row"><span><span class="legend-dot lr-dot"></span>Logistic Regression</span><span><span class="legend-dot rf-dot"></span>Random Forest</span></div>{bars_html}</div>',unsafe_allow_html=True)

    st.markdown('<div class="section">Confusion matrices</div><div class="sub">Actual classes versus model predictions on the test set.</div>',unsafe_allow_html=True)
    st.write('')
    def confusion_card(title,tn,fp,fn,tp):
        return f'''<div class="cm-card"><div class="cm-title">{title}</div><div class="cm-subtitle">Rows = actual &nbsp;•&nbsp; Columns = predicted</div><div class="cm-grid"><div class="cm-label corner"></div><div class="cm-label">Rejected</div><div class="cm-label">Approved</div><div class="cm-label side">Rejected</div><div class="cm-cell tn"><small>True Negative</small><strong>{tn}</strong></div><div class="cm-cell fp"><small>False Positive</small><strong>{fp}</strong></div><div class="cm-label side">Approved</div><div class="cm-cell fn"><small>False Negative</small><strong>{fn}</strong></div><div class="cm-cell tp"><small>True Positive</small><strong>{tp}</strong></div></div></div>'''
    c1,c2=st.columns(2,gap='large')
    with c1: st.markdown(confusion_card('Logistic Regression',280,43,30,501),unsafe_allow_html=True)
    with c2: st.markdown(confusion_card('Random Forest',315,8,8,523),unsafe_allow_html=True)

    st.markdown('<div class="section">Random Forest feature importance</div><div class="sub">Top five impurity-based feature importance values from the trained Random Forest.</div>',unsafe_allow_html=True)
    st.write('')
    features=[('CIBIL Score',79.55),('Loan Term',6.15),('Loan Amount',3.09),('Annual Income',1.95),('Luxury Assets Value',1.95)]
    feature_rows=''
    for name,value in features:
        width=(value/79.55)*100
        feature_rows += f'<div class="fi-row"><div class="fi-name">{name}</div><div class="fi-track"><div class="fi-fill" style="width:{width:.2f}%;"></div></div><div class="fi-value">{value:.2f}%</div></div>'
    st.markdown(f'<div class="perf-card"><div class="perf-card-head"><div><div class="perf-title">What the model relied on most</div><div class="perf-subtitle">Relative importance within the trained Random Forest</div></div><div class="importance-badge">Top 5</div></div>{feature_rows}<div class="table-note" style="margin-top:18px;">CIBIL Score is the dominant feature in the trained Random Forest model. Feature importance indicates model reliance, not causation.</div></div>',unsafe_allow_html=True)

    st.markdown('<div class="card" style="margin-top:20px;"><div style="font-size:20px;font-weight:850;color:#17394d;margin-bottom:8px;">Model selection</div><div class="muted" style="line-height:1.7;font-size:14px;">The project deploys Random Forest because its measured test-set performance was higher than Logistic Regression across the reported evaluation metrics. These results are specific to this project dataset and should not be interpreted as evidence of bank-grade or real-world lending performance.</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="footer">LoanLens AI • Model Evaluation Dashboard</div>',unsafe_allow_html=True)

if st.session_state.page=='home': home()
elif st.session_state.page=='assessment': assessment()
elif st.session_state.page=='performance': performance()
