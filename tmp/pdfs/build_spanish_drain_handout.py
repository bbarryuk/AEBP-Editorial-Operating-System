from pathlib import Path
from pypdf import PdfReader, PdfWriter
src = Path('tmp/pdfs/build_drain_handout.py').read_text(encoding='utf-8')
replacements = {
    'AEBP-Resident-Drain-Care.pdf': 'AEBP-Resident-Drain-Care-Spanish.pdf',
    'Keep Your Drains Flowing | All East Bay Properties': 'Cuide sus desagües | All East Bay Properties',
    "text(431,731,'RESIDENT GUIDE',10": "text(402,731,'GUÍA PARA RESIDENTES',10",
    "text(431,715,'Kitchen + Bathroom'": "text(402,715,'Cocina + Baño'",
    "'KEEP YOUR'": "'MANTENGA SUS'",
    "'DRAINS FLOWING',34": "'DESAGÜES LIBRES',32",
    "'Small habits help prevent clogs, backups and costly repairs.',11.5": "'Buenos hábitos previenen obstrucciones, desbordamientos y reparaciones costosas.',10.5",
    "'TOILETS: Only human waste and toilet paper.',13": "'INODOROS: Solo desechos humanos y papel higiénico.',12.5",
    "'BATHROOM'": "'BAÑO'", "'KITCHEN'": "'COCINA'", "'Keep these out'": "'No deseche lo siguiente'",
    "left=[['Baby / cleaning wipes, even','if labeled \"flushable\"'],['Paper towels and diapers'],['Feminine hygiene products'],['Cotton swabs, balls and makeup pads'],['Dental floss and hair'],['Medications and other chemicals']]": "left=[['Toallitas de bebé o de limpieza, aunque','digan que se pueden tirar al inodoro'],['Toallas de papel y pañales'],['Productos de higiene femenina'],['Hisopos, bolas de algodón y','discos desmaquillantes'],['Hilo dental y cabello'],['Medicamentos y otros químicos']]",
    "right=[['Grease, oil and cooking fat'],['Food scraps or large amounts of food'],['Coffee grounds and eggshells'],['Rice, pasta and foods that expand'],['Paper towels or wipes'],['Harsh chemicals and paint']]": "unused",
    "right=[['Grease, oil and cooking fat'],['Food scraps or large amounts of food'],['Coffee grounds and eggshells'],['Rice, pasta and foods that expand'],['Paper towels and wipes'],['Harsh chemicals and paint']]": "right=[['Grasa, aceite y manteca'],['Restos o grandes cantidades','de comida'],['Café molido usado y cáscaras de huevo'],['Arroz, pasta y alimentos','que se expanden'],['Toallas de papel y toallitas'],['Químicos fuertes y pintura']]",
    'lines(x+13,y,arr,10.8,14)': 'lines(x+13,y,arr,10.2,14)',
    'for a in right:bullet(328,y,a);y-=29': 'for a in right:bullet(328,y,a);y-=39 if len(a)>1 else 27',
    "'BETTER HABITS. FEWER BLOCKAGES.'": "'MEJORES HÁBITOS. MENOS OBSTRUCCIONES.'",
    "'BIN IT',['Put wipes, hygiene items','and food scraps in the trash.']": "'A LA BASURA',['Tire toallitas, artículos de higiene','y restos de comida a la basura.']",
    "'COOL IT',['Let grease cool; collect it','in a container for disposal.']": "'DEJE ENFRIAR',['Deje enfriar la grasa y recójala','en un recipiente para desecharla.']",
    "'DISPOSE SAFELY',['Use appropriate disposal for','medications, paint and chemicals.']": "'DESECHE CON CUIDADO',['Deseche medicamentos, pintura','y químicos de forma adecuada.']",
    'text(x+24,210,head,10': 'text(x+24,210,head,9',
    "'SLOW DRAIN, CLOG OR BACKUP?',12": "'¿DESAGÜE LENTO, ATASCADO O DESBORDADO?',11",
    "'24/7 MAINTENANCE  |  English / Spanish'": "'MANTENIMIENTO 24/7  |  Inglés / Español'",
    "'Open a work order through your resident portal:'": "'Solicite mantenimiento a través de su portal de residentes:'",
    "text(486,48,'Scan for portal',8": "text(480,48,'Escanee para entrar',8",
}
for old,new in replacements.items():
    if new == 'unused': continue
    assert old in src, old
    src=src.replace(old,new)
exec(compile(src,'spanish_layout','exec'))
out=Path('output/pdf')
writer=PdfWriter()
for filename in ['AEBP-Resident-Drain-Care.pdf','AEBP-Resident-Drain-Care-Spanish.pdf']:
    reader=PdfReader(out/filename)
    assert len(reader.pages)==1
    writer.append(reader)
writer.add_metadata({'/Title':'Drain Care | English + Español | All East Bay Properties'})
with (out/'AEBP-Resident-Drain-Care-Bilingual.pdf').open('wb') as f: writer.write(f)
assert len(PdfReader(out/'AEBP-Resident-Drain-Care-Bilingual.pdf').pages)==2
print('Verified Spanish page and bilingual two-page PDF.')
