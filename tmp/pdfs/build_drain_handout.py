from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from pypdf import PdfReader

OUT=Path('output/pdf'); OUT.mkdir(parents=True,exist_ok=True)
pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold','C:/Windows/Fonts/arialbd.ttf'))
N=HexColor('#151477'); R=HexColor('#E92329'); INK=HexColor('#252941'); MUT=HexColor('#596174'); BG=HexColor('#F3F5FA')
c=canvas.Canvas(str(OUT/'AEBP-Resident-Drain-Care.pdf'),pagesize=(612,792))
c.setTitle('Keep Your Drains Flowing | All East Bay Properties')
c.setAuthor('All East Bay Properties')
def text(x,y,s,size=11,color=INK,bold=False):
    c.setFillColor(color); c.setFont('Arial-Bold' if bold else 'Arial',size); c.drawString(x,y,s)
def box(x,y,w,h,color,r=12):
    c.setFillColor(color); c.roundRect(x,y,w,h,r,fill=1,stroke=0)
def lines(x,y,arr,size=11,leading=15,color=INK,bold=False):
    for a in arr: text(x,y,a,size,color,bold); y-=leading
def bullet(x,y,arr):
    c.setFillColor(R); c.circle(x+2,y+4,2,fill=1,stroke=0)
    lines(x+13,y,arr,10.8,14)
def icon(x,y,kind):
    c.saveState(); c.translate(x,y); c.setStrokeColor(N); c.setLineWidth(2.2)
    if kind=='toilet':
        c.roundRect(0,19,15,22,2,fill=0,stroke=1); c.line(15,23,39,23)
        p=c.beginPath();p.moveTo(4,19);p.curveTo(6,1,33,1,38,23); c.drawPath(p)
        c.line(16,6,13,-1); c.line(13,-1,32,-1);c.line(32,-1,28,7)
        c.line(4,34,8,34)
    else:
        c.roundRect(0,9,44,16,4,fill=0,stroke=1);c.line(22,25,22,37)
        p=c.beginPath();p.moveTo(22,37);p.curveTo(22,47,36,47,36,37); c.drawPath(p)
        c.line(36,37,36,33);c.line(12,9,12,0);c.line(32,9,32,0)
    c.restoreState()

c.setFillColor(N);c.rect(0,782,612,10,fill=1,stroke=0)
c.drawImage('C:/Users/brian/OneDrive - ALL EAST BAY PROPERTIES/Documents/AEP-logo/AEP-logo/AEBP-LOGOS/all-eastbay-logo-big.jpg',36,694,width=243,height=68.31)
text(431,731,'RESIDENT GUIDE',10,N,True)
text(431,715,'Kitchen + Bathroom',9,MUT)
text(36,659,'KEEP YOUR',30,N,True)
text(36,623,'DRAINS FLOWING',34,N,True)
text(36,596,'Small habits help prevent clogs, backups and costly repairs.',11.5,MUT)

box(36,535,540,43,N)
text(51,552,'TOILETS: Only human waste and toilet paper.',13,white,True)

for x in (36,313):box(x,263,263,256,BG)
icon(53,458,'toilet'); icon(330,458,'sink')
text(111,490,'BATHROOM',16,N,True);text(111,473,'Keep these out',10,R,True)
text(388,490,'KITCHEN',16,N,True);text(388,473,'Keep these out',10,R,True)
left=[['Baby / cleaning wipes, even','if labeled "flushable"'],['Paper towels and diapers'],['Feminine hygiene products'],['Cotton swabs, balls and makeup pads'],['Dental floss and hair'],['Medications and other chemicals']]
right=[['Grease, oil and cooking fat'],['Food scraps or large amounts of food'],['Coffee grounds and eggshells'],['Rice, pasta and foods that expand'],['Paper towels and wipes'],['Harsh chemicals and paint']]
y=438
for a in left: bullet(51,y,a);y-=39 if len(a)>1 else 27
y=438
for a in right:bullet(328,y,a);y-=29

text(36,239,'BETTER HABITS. FEWER BLOCKAGES.',13,N,True)
for x,num,head,body in [(36,'1','BIN IT',['Put wipes, hygiene items','and food scraps in the trash.']),(221,'2','COOL IT',['Let grease cool; collect it','in a container for disposal.']),(406,'3','DISPOSE SAFELY',['Use appropriate disposal for','medications, paint and chemicals.'])]:
    c.setFillColor(R);c.circle(x+9,214,9,fill=1,stroke=0);text(x+6,210,num,10,white,True)
    text(x+24,210,head,10,N,True);lines(x,190,body,9.2,13,MUT)

box(36,36,540,122,N)
text(52,137,'SLOW DRAIN, CLOG OR BACKUP?',12,white,True)
text(52,104,'510-450-3815',27,white,True)
text(52,85,'24/7 MAINTENANCE  |  English / Spanish',10.5,white,True)
text(52,65,'Open a work order through your resident portal:',9,white)
url='https://alleastbayproperties.appfolio.com/connect'
text(52,50,'alleastbayproperties.appfolio.com/connect',9.3,white)
c.linkURL(url,(52,46,332,60),relative=0,thickness=0)
c.linkURL('tel:+15104503815',(52,98,294,128),relative=0,thickness=0)
box(480,61,79,79,white,4)
q=qr.QrCodeWidget(url); b=q.getBounds(); d=Drawing(75,75,transform=[75/(b[2]-b[0]),0,0,75/(b[3]-b[1]),0,0]);d.add(q);renderPDF.draw(d,c,482,63)
text(486,48,'Scan for portal',8,white)
text(36,20,'2324 Powell St. Emeryville, CA 94608',9,MUT)
text(486,20,'CalDRE: 01516255',9,MUT)
c.showPage();c.save()
r=PdfReader(OUT/'AEBP-Resident-Drain-Care.pdf')
assert len(r.pages)==1
assert '510-450-3815' in r.pages[0].extract_text()
assert '2324 Powell St. Emeryville, CA 94608' in r.pages[0].extract_text()
assert 'CalDRE: 01516255' in r.pages[0].extract_text()
print('Verified one-page PDF and maintenance number.')
