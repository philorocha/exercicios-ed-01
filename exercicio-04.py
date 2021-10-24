ranking_medalhas = "Estados Unidos", "China", "Japão", "Grã-Bretanha", "Russia", "Austrália", "Holanda", "França", "Alemanha", "Itália", "Canadá", "Brasil", "Nova Zelândia", "Cuba", "Hungria"

print(f"Três primeiros colocados: {ranking_medalhas[:3]}")
print(f"Dois últimos colocados: {ranking_medalhas[-2:]}")

if "Brasil" in ranking_medalhas[:15]:
    print(f"Posição do Brasil no rank: {ranking_medalhas.index('Brasil') + 1}")