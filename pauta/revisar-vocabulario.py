import re,sys
# Términos que no deben aparecer en anuncios de Zafira (proyecto + Meta citas/atributos personales)
BAN=[r"\bevents?\b",r"\beventos?\b",r"\bexperiences?\b",r"\bexperiencias?\b",r"\blatin[ao]s?\b",r"latinoamerican",
     r"\bbrides?\b",r"\bnovias?\b",r"mail[- ]order",r"catalog",r"\bwomen\b",r"\bmujeres\b",r"\bbeautiful\b",r"\bhot\b",
     r"\byoung\b",r"\bsexy\b",r"\bvisas?\b",r"\bguarantee(d|s)?\b(?!.*no)",r"\bsingles?\b",r"\bdivorc",r"\blonely\b",
     r"\bover \d+\b",r"\bonly \d+ (spots|places)\b",r"\blimited (spots|places)\b",r"\bforeign\b",r"\bexotic\b",r"\bgirls?\b",
     r"are you\b",r"\bcompanionship\b",r"\bescort"]
txt=open(sys.argv[1]).read()
sec=txt[txt.index("## Anuncios"):txt.index("## Revisión de vocabulario")]
hits=[(b,m.group(0)) for b in BAN for m in re.finditer(b,sec,re.I)]
print("Texto revisado: sección 'Anuncios' de",sys.argv[1])
print("Términos prohibidos encontrados:",len(hits))
for b,h in hits: print("  -",h,"(regla",b,")")
