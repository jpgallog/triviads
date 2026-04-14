import os
import json

base_dir = "/Users/jpgallog/Documents/Antigravity/triviads"

# 1. STYLE.CSS
with open(os.path.join(base_dir, "style.css"), "a") as f:
    f.write("\n\n/* Language Switch */\n")
    f.write(".lang-switch-container {\n  position: absolute;\n  top: 20px;\n  right: 20px;\n  display: flex;\n  align-items: center;\n  gap: 8px;\n  font-weight: 600;\n  font-size: 0.9rem;\n  color: #777;\n  z-index: 10;\n}\n")
    f.write(".lang-label {\n  cursor: pointer;\n  transition: color 0.3s;\n}\n")
    f.write(".lang-label.active {\n  color: var(--meli-blue);\n  font-weight: 800;\n}\n")
    f.write(".switch {\n  position: relative;\n  display: inline-block;\n  width: 44px;\n  height: 24px;\n}\n")
    f.write(".switch input { \n  opacity: 0;\n  width: 0;\n  height: 0;\n}\n")
    f.write(".slider {\n  position: absolute;\n  cursor: pointer;\n  top: 0; left: 0; right: 0; bottom: 0;\n  background-color: #ccc;\n  transition: .4s;\n}\n")
    f.write(".slider:before {\n  position: absolute;\n  content: \"\";\n  height: 18px;\n  width: 18px;\n  left: 3px;\n  bottom: 3px;\n  background-color: white;\n  transition: .4s;\n}\n")
    f.write("input:checked + .slider {\n  background-color: var(--meli-light-blue);\n}\n")
    f.write("input:focus + .slider {\n  box-shadow: 0 0 1px var(--meli-light-blue);\n}\n")
    f.write("input:checked + .slider:before {\n  transform: translateX(20px);\n}\n")
    f.write(".slider.round {\n  border-radius: 24px;\n}\n")
    f.write(".slider.round:before {\n  border-radius: 50%;\n}\n")

# 2. QUESTIONS.JS
q_js = """export const questions = {
  es: [
    { question: "¿Qué métrica indica el costo promedio que pagas por cada clic en tu anuncio?", options: ["CPM", "CTR", "CPC", "ACOS"], correctAnswer: 2, explanation: "El CPC (Costo Por Clic) se calcula dividiendo la inversión total por el número de clics.", difficulty: "facil" },
    { question: "Para medir posicionamiento de marca y exposición, ¿qué métrica debe optimizarse?", options: ["CPA", "CPM", "CPC", "CPL"], correctAnswer: 1, explanation: "El CPM (Costo por Mil Impresiones) te ayuda a maximizar tu visibilidad a gran escala en estrategias de branding.", difficulty: "facil" },
    { question: "¿Qué indica la precisión de tu anuncio, es decir, qué porcentaje de la gente decide al menos verlo de cerca?", options: ["ACOS", "ROAS de Búsqueda", "CTR", "CVR"], correctAnswer: 2, explanation: "El CTR (Click-Through Rate) muestra cuántos clics obtuviste por la cantidad de veces que se imprimió tu anuncio.", difficulty: "facil" },
    { question: "La Tasa de Conversión (CVR) representa:", options: ["Las impresiones brutas del anuncio", "Qué porcentaje de los clics se convirtieron en compras", "El costo por lograr que un cliente vuelva", "Segmentación fallida"], correctAnswer: 1, explanation: "Una buena tasa de conversión (CVR) significa que tu landing page o página de producto convence efectivamente al usuario de comprar.", difficulty: "facil" },
    { question: "¿Qué es una 'Impresión' en publicidad digital?", options: ["El costo de imprimir folletos", "La cantidad de veces que se muestra un anuncio en la pantalla de un usuario", "La sensación que le deja la marca al comprador", "Un clic exitoso"], correctAnswer: 1, explanation: "Cada vez que tu anuncio carga y se despliega en pantalla es contabilizado como 1 Impresión.", difficulty: "facil" },
    { question: "En Mercado Ads, ¿Qué es el 'Presupuesto Diario'?", options: ["Lo que el usuario gasta al comprar", "El límite de dinero que Mercado Libre te presta para publicidad", "El monto máximo preestablecido que estás dispuesto a invertir por día en una campaña", "Un seguro mensual"], correctAnswer: 2, explanation: "Establecer tu presupuesto diario controla tus recursos financieros limitando lo máximo a consumir en el día publicitario.", difficulty: "facil" },
    { question: "¿Qué hace que la publicidad dentro de un Marketplace (como Mercado Libre) sea tan efectiva?", options: ["No tiene competencia de precios", "Hay pauta en la televisión de forma gratis", "Alcanzas a usuarios con una fuerte intención de búsqueda y de compra real", "Genera likes automáticamente"], correctAnswer: 2, explanation: "Los usuarios ya están navegando listos para comprar, impactarlos ahí potencia la efectividad radicalmente frente a otras redes sociales.", difficulty: "facil" },
    { question: "¿Qué efecto tiene poner en 'Pausa' una campaña publicitaria?", options: ["Los anuncios se siguen mostrando, pero gratis", "Detiene al instante la entrega de anuncios y el consumo de inversión", "Reduce el costo a la mitad", "Los envíos se vuelven gratis"], correctAnswer: 1, explanation: "Pausar es la acción instantánea para cortar o detener el ritmo de gasto si tienes que restructurar métricas.", difficulty: "facil" },
    { question: "¿Qué significa el término 'Clic' en nuestro contexto publicitario?", options: ["Cuando un cliente agrega al carrito", "La acción donde el usuario oprime el anuncio y es llevado al producto/página", "Una interacción telefónica", "El pago de un producto en cuotas"], correctAnswer: 1, explanation: "El clic comprueba que tu pieza creativa o banner logró atraer la suficiente atención del usuario.", difficulty: "facil" },
    { question: "¿Cuál de los siguientes es el propio ecosistema de soluciones publicitarias integrado de Mercado Libre?", options: ["Mercado Shops", "Mercado Envíos", "Mercado Pago", "Mercado Ads"], correctAnswer: 3, explanation: "Mercado Ads nuclea todas las herramientas (Performance, Display, etc.) para acelerar ventas de anunciantes en MELI.", difficulty: "facil" },

    { question: "¿Qué significan las siglas ROAS?", options: ["Return On Ad Spend (Retorno sobre Inversión Publicitaria)", "Rate of Advertising Sales", "Return On Actual Sales", "Revenue over Ad Spend"], correctAnswer: 0, explanation: "El ROAS mide los ingresos generados por cada peso o dólar invertido en publicidad.", difficulty: "intermedio" },
    { question: "¿Qué nos muestra el 'Share of Voice' (SOV)?", options: ["El porcentaje de mercado publicitario y visibilidad que logramos frente a todos nuestros competidores", "Porcentaje de quejas al call-center por un producto defectuoso", "Búsquedas realizadas por micrófono", "Costos en campañas auditivas"], correctAnswer: 0, explanation: "Un alto Share of Voice significa que tu marca domina la cuota de pantalla frente a las demás alternativas.", difficulty: "intermedio" },
    { question: "¿Qué término hace referencia a la adquisición de tráfico logrando una venta, acción o subscripción?", options: ["CPV", "CPA", "CPM", "CTa"], correctAnswer: 1, explanation: "El CPA (Costo Por Adquisición) se basa en la meta final de negocio o performance máxima para registrar leads o conversiones reales.", difficulty: "intermedio" },
    { question: "¿Para qué sirve 'Product Ads' dentro de Mercado Libre?", options: ["Enviar correos publicitarios masivos", "Potenciar y apalancar posiciones destacadas del producto dentro de búsquedas relevantes en el sitio", "Aparecer en carteleras de vía pública", "Comprar inventario remanente de Youtube"], correctAnswer: 1, explanation: "La herramienta Product Ads mejora la exposición del catálogo empujando los ítems a los top slots dentro de las subpáginas o listados.", difficulty: "intermedio" },
    { question: "¿Qué rige y evalúa el modelo de 'Subasta' (Bidding) detrás de Product Ads?", options: ["Un algoritmo donde solo importa tener el producto más barato a la venta", "Un sistema donde ganas exposición combinando e impactando tu límite de oferta (CPC) y la calidad intrínseca de tu anuncio", "Pagar una cuota fija manual mensual", "El mejor vendedor siempre gana el primer lugar sin pagar Ads"], correctAnswer: 1, explanation: "Es un balance vital; por más que pagues mucho CPC, si tu Ad no tiene relevancia orgánica (Calidad), pierdes la subasta.", difficulty: "intermedio" },
    { question: "¿Qué es una estrategia 'Always On'?", options: ["Tener la tienda online sin contraseñas locales", "Campañas tácticas que solo levantan alcance durante eventos únicos como Hot Sale", "Tener publicidad activa de forma ininterrumpida para abarcar la demanda constante", "Apagar campañas y dejarlas offline en horarios nocturnos"], correctAnswer: 2, explanation: "Estar siempre prendido asegura que ningún comprador potencial de tu nicho se esfume por falta de publicidad activa diaria.", difficulty: "intermedio" },
    { question: "¿A qué etapa del Pipeline o Funnel (Embudo) ataca preferentemente Product Ads?", options: ["Upper Funnel (Awareness/Notoriedad a gran escala)", "Lower Funnel (Conversión y Ventas transaccionales directas)", "Mid Funnel Exclusivo (Consideración Pura)", "Soporte de fidelización Post-compra y Mails"], correctAnswer: 1, explanation: "Dado que el cliente está buscando con alta intención un ítem, Product Ads cierra directamente su viaje con el clic y posterior compra local.", difficulty: "intermedio" },
    { question: "Si queremos aparecer ante intenciones específicas del cliente que redacta en el buscador, deberíamos utilizar estratégicamente:", options: ["Palabras Clave (Keywords)", "Emojis llamativos en el banner", "Pauta televisiva local", "Display Banners masivos del sitio"], correctAnswer: 0, explanation: "Alinear palabras clave como match garantiza que te cruces cuando el cliente tipée tu rubro.", difficulty: "intermedio" },
    { question: "¿Por qué Mercado Ads califica la 'Relevancia' del anuncio al decidir el ganador final de una subasta de impresión?", options: ["Para cobrarle siempre al vendedor más adinerado", "Para garantizar que el comprador vea publicidad acorde y no frustrante a lo que busca, logrando fluidez de ecosistema", "Porque bloquea las publicaciones con envío gratis automático", "Para descartar productos provenientes del exterior arbitrariamente"], correctAnswer: 1, explanation: "La Relevancia prioriza el engagement del usuario: si busca Laptops y tú le muestras Lavadoras, empeoras brutalmente la experiencia de compra.", difficulty: "intermedio" },
    { question: "En métricas publicitarias ¿A qué llamamos y qué se entiende por 'Ventana de Atribución'?", options: ["El margen y ventana de tiempo dictaminado en el que un clic pasado sigue influyendo e hilvanando la adjudicación y el mérito de una venta", "El momento o día del mes en que se facturan los consumos en tarjetas", "El recuadro o popup limitante que bloquea un anuncio emergente publicitario", "Tiempo final de garantía y vida útil de inventario"], correctAnswer: 0, explanation: "Define cuánto tiempo (ej: 7 días, 14 días) un evento de pago (la compra) pertenece y es acreditado lógicamente por un Clic en un Ad anterior.", difficulty: "intermedio" },

    { question: "¿Cómo se mide la salud de la inversión en campañas de Performance en Mercado Libre?", options: ["Tasa de rebote orgánico", "ACOS", "Click-Through Rate exclusivo", "CPV"], correctAnswer: 1, explanation: "El ACOS (Advertising Cost of Sales) refleja qué porcentaje de tu dinero generado en la venta consumió la publicidad.", difficulty: "dificil" },
    { question: "¿Qué es el Retargeting?", options: ["Anunciar exclusivamente a usuarios que ya mostraron interés previo en tu producto o marca", "Configurar los costos a un límite mensual", "Cambiar la agencia creativa regularmente", "Eliminar palabras clave negativas"], correctAnswer: 0, explanation: "El Retargeting permite volver a capturar la atención de usuarios potenciales más proclives a concretar.", difficulty: "dificil" },
    { question: "¿Cuál es el principal valor de usar 'Custom Audiences' (Audiencias Diferenciadas)?", options: ["Te obligan a mantener siempre el mismo banner", "Garantizan siempre 100% de conversión cruzada", "Permiten apuntar a consumidores a partir de sus intenciones reales y comportamientos de navegación previos predominantes", "Son más baratas siempre"], correctAnswer: 2, explanation: "Con Custom Audiences le llegas directamente a aquel cliente altamente relevante usando Inteligencia de los sitios en la red de Mercado Ads.", difficulty: "dificil" },
    { question: "Dentro de la medición de Display Ads, Viewability garantiza estrictamente que...", options: ["El anuncio corrió masivamente en TV sin interrupción", "El banner tuvo la debida visibilidad parcial de pixeles en foco de pantalla por los segundos formativos estandarizados por la industria", "El banner generó una viralización social inmediata", "El archivo de arte y vector se descargó ultra rápido en la SD local del móvil del navegante"], correctAnswer: 1, explanation: "Viewability certifica para las grandes agencias que sí obtuvieron presencia de ojos en el plano digital de su mercado meta.", difficulty: "dificil" },
    { question: "¿Qué métrica vital usarías si estás comprando en programático y solo exiges optimizar tu pago basándote puntualmente en impresiones que validamente entraron en la vista real del humano?", options: ["CTR general de las Imágenes", "CPV Base", "vCPM (Cost per viewable 1,000 impressions)", "Mediana Frecuencia Absoluta"], correctAnswer: 2, explanation: "Diferente al simple CPM, el vCPM destina rigor de auditoría para pagar por exposición confirmada on-screen, fundamental en Brand Awareness.", difficulty: "dificil" },
    { question: "Para que el pilar predictivo de Machine Learning de la campaña madure y salga exitosamente de su 'fase ciega de aprendizaje', estadísticamente carecerá y necesitará de:", options: ["Exceder radicalmente el presupuesto del Marketplace", "Simplificar e inhibir palabras a usar un nombre más críptico o corto", "Llegar y englobar rápidamente un gran volumen de tracción algorítmica constante como clics o conversiones en ventana inicial", "Usar arbitrariamente todas las intenciones posibles como palabras clave negativas cruzadas"], correctAnswer: 2, explanation: "El modelo predictivo no es mago; requiere combustible o 'Data'. Ese dato son las conversiones. Más data = aprendizaje superado y optimizado.", difficulty: "dificil" },
    { question: "El arsenal de 'First-Party Data' empaquetado y crudo de Mercado Libre rompe la media del e-commerce moderno y la industria ya que...", options: ["Lee sin cifrar el tracking geo satelital profundo o chats genéricos del browser", "Rastrea localmente con contraseñas bancarias y burocracia ajena o federal", "Clasifica y permite proyectar e influir basándose en comportamientos verídicos, pagos y propensiones finalizadas de compras concretas de la red", "Permite ver e intervenir nativamente la historia completa de a qué otras páginas externas entra el comprador luego"], correctAnswer: 2, explanation: "Al no depender de redes de terceros, MELI posee la certeza cruda e inequívoca de si compraron, cuánto y cuándo interesó; un pilar en un futuro sin 3rd-party cookies.", difficulty: "dificil" },
    { question: "Si tu empresa produce de cero y vende Zapatillas Exclusivas de asfalto y deportivas, ¿Por qué estratégicamente apilarías 'Usadas' como Palabra Clave Negativa Exacta dentro de tu matriz?", options: ["Porque restringe contundentemente tirar y malgastar presupuesto con clics transeúntes de usuarios cazadores abocados meramente a mercado secundario", "Para desviar algorítmicamente envíos de correos hacia el país lejano de destino", "Por que Mercado Ads bloquea automáticamente y penaliza publicitar artículos importados indirectamente", "Para inflar e ilusionar en un 40% tu ACOS base matemáticamente"], correctAnswer: 0, explanation: "El tráfico no deseado (ej. buscar segunda mano) se corta de raíz con Negative Keywords, liberando capital o wallet para tu verdadera audiencia que busca tu Ítem Cero KM.", difficulty: "dificil" },
    { question: "En un escenario Programático de Display / Performance transversal, un sistema robusto nativo o algorítmico de 'Pacing' asegura fuertemente:", options: ["Pausar y blindar totalmente en banda baja hasta validar el scoring total en tu tarjeta local confirmando saldo de origen", "Reducir y comprimir audios, acelerando metadatos para optimizar peso multimedia estricto y banda de impacto", "Distribuir e inyectar progresivamente consumos monetarios durante el transcurso lineal dictaminado con el fin de evitar quemar y quedarse sin el grueso presupuestal de la cuenta en las frenéticas primeras horas de mañana o picos", "Registrar y neutralizar temporalmente el frenético clic o las intenciones maliciosas de clicks bots invalidando pulsaciones rápidas repetidas por IP"], correctAnswer: 2, explanation: "El 'Pacing' orquesta un presupuesto diario ej:$1000 en todo tu día para que a las 5PM aún tengas alcance activo si alguien te busca para comprar, y no gastarlo a las 11AM limitando presencia vespertina.", difficulty: "dificil" },
    { question: "¿A qué denominamos métricamente la variable y ratio de Venta o 'Conversión Incremental' asociada unívocamente tras arrancar las campañas experimentales?", options: ["Las estimaciones macro diarias y brutas proyectadas a 1 año fiscal sin interrupción lineal basada en picos de Cybermonday pasados", "Decodifica el lote de compras logradas en alza total y puramente gracias a los anuncios en Ads, aislando qué no habrían ocurrido orgánicamente solas o si detuvieses abruptamente la inversión", "Se adjudica y extrapola todas las ventas hechas por tus competidores por la causa directa indirecta y tracción de rebote hacia tus anuncios parpadeantes", "Alude al crecimiento estricto orgánico nominal e indirecto de comisiones que cobra toda la plataforma por tu uso del modelo FULL de envíos gratuitos obligatorios de retención"], correctAnswer: 1, explanation: "La Incrementabilidad aísla tu canibalismo: responde a la máxima interrogante del marketer: '¿Hubieran comprado de todos modos?'. Mide qué plus y margen real genuino originó la campaña aislada que ni hubiera ocurrido per se. ROAS es solo la foto general; Incrementabilidad es el valor verdadero ganado.", difficulty: "dificil" }
  ],
  pt: [
    { question: "Qual métrica indica o custo médio que você paga por cada clique no seu anúncio?", options: ["CPM", "CTR", "CPC", "ACOS"], correctAnswer: 2, explanation: "O CPC (Custo Por Clique) é calculado dividindo o investimento total pelo número de cliques.", difficulty: "facil" },
    { question: "Para medir o posicionamento da marca e a exposição, qual métrica deve ser otimizada?", options: ["CPA", "CPM", "CPC", "CPL"], correctAnswer: 1, explanation: "O CPM (Custo por Mil Impressões) ajuda a maximizar sua visibilidade em larga escala em estratégias de branding.", difficulty: "facil" },
    { question: "O que indica a precisão do seu anúncio, ou seja, qual porcentagem das pessoas decide pelo menos vê-lo de perto?", options: ["ACOS", "ROAS de Busca", "CTR", "CVR"], correctAnswer: 2, explanation: "O CTR (Click-Through Rate) mostra quantos cliques você obteve divididos pela quantidade de vezes que seu anúncio foi impresso.", difficulty: "facil" },
    { question: "A Taxa de Conversão (CVR) representa:", options: ["As impressões brutas do anúncio", "Que porcentagem dos cliques se converteu em compras", "O custo para fazer um cliente voltar", "Segmentação falha"], correctAnswer: 1, explanation: "Uma boa taxa de conversão (CVR) significa que sua landing page ou página de produto convence efetivamente o usuário a comprar.", difficulty: "facil" },
    { question: "O que é uma 'Impressão' na publicidade digital?", options: ["O custo de imprimir folhetos", "A quantidade de vezes que um anúncio é mostrado na tela de um usuário", "A sensação que a marca deixa no comprador", "Um clique bem-sucedido"], correctAnswer: 1, explanation: "Cada vez que seu anúncio carrega e é exibido na tela, é contabilizado como 1 Impressão.", difficulty: "facil" },
    { question: "No Mercado Ads, o que é o 'Orçamento Diário'?", options: ["O que o usuário gasta ao comprar", "O limite de dinheiro que o Mercado Livre empresta para publicidade", "O valor máximo pré-estabelecido que você está disposto a investir por dia em uma campanha", "Um seguro mensal"], correctAnswer: 2, explanation: "Estabelecer seu orçamento diário controla seus recursos financeiros, limitando o máximo a ser consumido no dia publicitário.", difficulty: "facil" },
    { question: "O que torna a publicidade dentro de um Marketplace (como Mercado Livre) tão efetiva?", options: ["Não tem concorrência de preços", "Há publicidade na televisão de forma grátis", "Você alcança usuários com uma forte intenção de busca e de compra real", "Gera likes automaticamente"], correctAnswer: 2, explanation: "Os usuários já estão navegando prontos para comprar, impactá-los lá potencializa a eficácia radicalmente em comparação com outras redes sociais.", difficulty: "facil" },
    { question: "Qual é o efeito de 'Pausar' uma campanha publicitária?", options: ["Os anúncios continuam sendo exibidos, mas gratuitamente", "Interrompe instantaneamente a entrega de anúncios e o consumo de investimento", "Reduz o custo pela metade", "Os envios tornam-se gratuitos"], correctAnswer: 1, explanation: "Pausar é a ação instantânea para cortar ou interromper o ritmo de gastos se você precisar restruturar as métricas.", difficulty: "facil" },
    { question: "O que significa o termo 'Clique' no nosso contexto publicitário?", options: ["Quando um cliente adiciona ao carrinho", "A ação em que o usuário pressiona o anúncio e é levado ao produto/página", "Uma interação telefônica", "O pagamento de um produto parcelado"], correctAnswer: 1, explanation: "O clique comprova que sua peça criativa ou banner conseguiu atrair a atenção suficiente do usuário.", difficulty: "facil" },
    { question: "Qual dos seguintes é o ecossistema próprio de soluções publicitárias integrado do Mercado Livre?", options: ["Mercado Shops", "Mercado Envios", "Mercado Pago", "Mercado Ads"], correctAnswer: 3, explanation: "O Mercado Ads centraliza todas as ferramentas (Performance, Display, etc.) para acelerar as vendas dos anunciantes no MELI.", difficulty: "facil" },

    { question: "O que significa a sigla ROAS?", options: ["Return On Ad Spend (Retorno sobre Investimento Publicitário)", "Rate of Advertising Sales", "Return On Actual Sales", "Revenue over Ad Spend"], correctAnswer: 0, explanation: "O ROAS mede a receita gerada por cada real ou dólar investido em publicidade.", difficulty: "intermedio" },
    { question: "O que o 'Share of Voice' (SOV) nos mostra?", options: ["A porcentagem do mercado publicitário e a visibilidade que alcançamos em comparação com todos os nossos concorrentes", "A porcentagem de reclamações no call-center por um produto com defeito", "As buscas realizadas por microfone", "Os custos em campanhas de áudio"], correctAnswer: 0, explanation: "Um alto Share of Voice significa que sua marca domina o espaço da tela em relação às outras alternativas.", difficulty: "intermedio" },
    { question: "Qual termo se refere à aquisição de tráfego que resulta em uma venda, ação ou assinatura?", options: ["CPV", "CPA", "CPM", "CTa"], correctAnswer: 1, explanation: "O CPA (Custo Por Aquisição) baseia-se na meta final de negócios ou na performance máxima para registrar leads ou conversões reais.", difficulty: "intermedio" },
    { question: "Para que serve o 'Product Ads' dentro do Mercado Livre?", options: ["Para enviar e-mails publicitários em massa", "Para potencializar e alavancar posições de destaque do produto em pesquisas relevantes no site", "Para aparecer em painéis de publicidade nas ruas", "Para comprar inventário remanescente do Youtube"], correctAnswer: 1, explanation: "A ferramenta Product Ads melhora a exposição do catálogo impulsionando os itens para as primeiras posições nas subpáginas ou listas.", difficulty: "intermedio" },
    { question: "O que rege e avalia o modelo de 'Leilão' (Bidding) por trás do Product Ads?", options: ["Um algoritmo onde o importante é ter o produto mais barato à venda", "Um sistema onde você ganha exposição combinando e impactando seu limite de lance (CPC) e a qualidade intrínseca do seu anúncio", "Pagar uma taxa fixa manual mensal", "O melhor vendedor sempre ganha o primeiro lugar sem pagar por Ads"], correctAnswer: 1, explanation: "É um equilíbrio vital; mesmo pagando muito pelo CPC, se o seu anúncio não tiver relevância orgânica (Qualidade), você perde o leilão.", difficulty: "intermedio" },
    { question: "O que é uma estratégia 'Always On'?", options: ["Manter a loja online sem senhas locais", "Campanhas táticas que apenas aumentam o alcance durante eventos únicos como Hot Sale", "Manter a publicidade ativa de forma ininterrupta para cobrir a demanda constante", "Desativar as campanhas e deixá-las offline durante a noite"], correctAnswer: 2, explanation: "Estar sempre ativo garante que nenhum comprador em potencial no seu nicho escape devido à falta de publicidade ativa diariamente.", difficulty: "intermedio" },
    { question: "Qual estágio do Funil (Pipeline) o Product Ads ataca preferencialmente?", options: ["Upper Funnel (Notoriedade/Awareness em larga escala)", "Lower Funnel (Conversão e Vendas transacionais diretas)", "Mid Funnel Exclusivo (Consideração Pura)", "Suporte e fidelização de e-mails pós-compra"], correctAnswer: 1, explanation: "Como o cliente já busca com alta intenção, o Product Ads encerra a jornada dele diretamente com o clique e posterior compra.", difficulty: "intermedio" },
    { question: "Se quisermos aparecer para intenções específicas do cliente ao digitar no mecanismo de busca, devemos usar de forma estratégica:", options: ["Palavras-chave (Keywords)", "Emojis chamativos no banner", "Publicidade na televisão local", "Banners massivos de Display no site"], correctAnswer: 0, explanation: "Alinhar palavras-chave como correspondência garante que o seu anúncio seja exibido quando o cliente pesquisar pela sua área.", difficulty: "intermedio" },
    { question: "Por que o Mercado Ads califica a 'Relevância' do anúncio ao decidir o vencedor final de um leilão de impressão?", options: ["Para sempre cobrar mais do vendedor mais rico", "Para garantir que o comprador veja anúncios relevantes e não frustrantes de acordo com o que busca, garantindo fluidez ao ecossistema", "Porque ele bloqueia os anúncios com frete grátis automático", "Para descartar arbitrariamente os produtos provenientes do exterior"], correctAnswer: 1, explanation: "A Relevância prioriza a experiência do usuário: se alguém procura Laptops e você exibe Máquinas de lavar, a experiência de compra é arruinada.", difficulty: "intermedio" },
    { question: "Nas métricas publicitárias, o que significa a 'Janela de Atribuição'?", options: ["O limite de tempo no qual um clique passado continua influenciando e gerando adjudicação e crédito de uma venda", "A hora ou dia do mês em que o consumo é faturado nos cartões", "A caixa delimitadora ou pop-up que bloqueia um anúncio publicitário", "O fim da garantia ou vida útil de inventário"], correctAnswer: 0, explanation: "Ela define quanto tempo (por exemplo, 7 ou 14 dias) uma compra pertence logicamente e é creditada a um clique anterior.", difficulty: "intermedio" },

    { question: "Como se mede a saúde do investimento em campanhas de Performance no Mercado Livre?", options: ["Taxa de rejeição", "ACOS", "Apenas pelo Click-Through Rate", "CPV"], correctAnswer: 1, explanation: "O ACOS (Custo de Vendas Publicitárias) reflete a porcentagem da receita das suas vendas que as despesas com publicidade consumiram.", difficulty: "dificil" },
    { question: "O que é o Retargeting?", options: ["Anunciar exclusivamente aos usuários que já demonstraram interesse prévio em seu produto ou na sua marca", "Limitar os custos mensais", "Trocar regularmente a agência de publicidade", "Excluir palavras-chave negativas"], correctAnswer: 0, explanation: "O Retargeting permite que você alcance usuários em potencial, com maior probabilidade de converter e de concluir a desejada compra.", difficulty: "dificil" },
    { question: "A principal vantagem em criar 'Custom Audiences' (Públicos Personalizados) é:", options: ["Exige manter um igual estilo de banners.", "Eles têm 100% conversões em vendas.", "Atingir os consumidores através de interesses e o engajamento baseados num bom conhecimento das visitas em web. ", "Costumam possuir descontos publicitários em cliques."], correctAnswer: 2, explanation: "Usar Custom Audiences permite ao usuário interagir em publicidade com quem busca anúncios diretamente ao vivo no Mercado Livre. ", difficulty: "dificil" },
    { question: "Dentro da medição de Display Ads, o Viewability garante estritamente que...", options: ["O anúncio foi exibido na TV maciçamente sem interrupções", "O banner obteve a debida visibilidade de pixels focados em tela por segundos de padrões exigidos por certificadoras de internet", "O banner gerou repercussões enormes nas redes socias do utilizador.", "O design em gráficos transferiu um código rápido no armazenamento na memoria ram local das abas do espectador."], correctAnswer: 1, explanation: "O Viewability certifica para a auditoria profissional do anunciante uma visualização concreta no site de origem. ", difficulty: "dificil" },
    { question: "Qual a medição exata para exigir o reembolso publicitário de apenas métricas reais e visuais dos anúncios programáticos?", options: ["CTR padrão das estampas", "CPV de alcance.", "vCPM (O Custo Por 1,000 Impressões Visíveis ) ", "Média da Taxa Constante"], correctAnswer: 2, explanation: "Ao invés de comprar visualizações de telas ocultas, paga-se ao monitor e comprovação humana apenas, para garantir eficácia. ", difficulty: "dificil" },
    { question: "No pilar da ferramenta das métricas de IA de publicidade para superar e conseguir crescer na 'fase escondida e em amadurecimento' precisará:", options: ["Ter aumento absurdo do limite creditório para uso.", "Encurtar nomenclaturas dificultosas aos buscadores modernos", "Adquirir informações contínuas na janela semanal ou tracionar rapidamente o público alvo usando os cliques no início da fase", "Incluir totalmente nomes que inibem o contato."], correctAnswer: 2, explanation: "O banco de dados algorítmico avalia tendências de conversão online, os movimentos do visitante e o perfil da aba do dispositivo.", difficulty: "dificil" },
    { question: "A vantagem dos Dados Primários ou (First-Party Data) da plataforma oficial no controle atual frente o concorrente eletrônico consiste em...", options: ["Monitoramento profundo digital através dos GPS satélite ou registros SMS dos provedores web. ", "Bases rastreáveis de instituições oficiais e bancárias com impostos inclusos locais", "Segmentações do comprador usando registros das interações online da rede de compras verídicas sem redes avulsas. ", "Manipulações na leitura orgânica de outros sites"], correctAnswer: 2, explanation: "A certeza é garantida por monitorizar cada visualização sem usar terceiros na validação algorítmica ou cookes que decaem facilmente. ", difficulty: "dificil" },
    { question: "Quando alguém começa um projeto de Calçados da sua Categoria, por qual razão estratégica bloquearia a Expressão Exata 'Usados' em Palavras-chave Negativas num Painel de Publicidade?", options: ["Eliminar de fato as perdas de lucro num comprador do âmbito virtual buscando em sites secundários ", "Destinar envios dos caminhões à logística no exterior de forma imediata à alfandega", "Para não contrariar regras ou ser suspenso devido a pirataria ou de um objeto clandestino regional", "Alterar as planilhas bancárias ao sistema analítico. "], correctAnswer: 0, explanation: "Filtrar por palavras limitadoras ajuda não só ao usuário não procurar em anúncios inúteis do anunciante; pois protege assim do encerramento das vendas online ", difficulty: "dificil" },
    { question: "Um sistema algorítmico robusto do Pacing usado perante um planejamento programático da audiência de Mídia protege ativamente contra o quê? ", options: ["Paralisia forçada no banco digital na confirmação inicial sobre faturas financeiras ao exterior", "Gasto de dados ou memória virtual numa internet fraca ou de pacotes lentos ao cliente ", "Investimento perdido, já que os dispêndios orçamentais daquele limite durarão o dia inteiro para os demais públicos na jornada online e evitar o esgotamento precoce diário ", "Vírus na segurança que simulam as métricas das atividades não humanas, excluindo endereços de Internet local fraudulenta"], correctAnswer: 2, explanation: "É a ferramenta preventiva sobre o saldo; onde sem ele, seu dinheiro na campanha matutina é consumido em questão de 60 minutos ou as primeiras horas.", difficulty: "dificil" },
    { question: "Como métrica e valor no contexto dos relatórios, o sentido ou entendimento puro de 'Conversão Incremental' aponta essencialmente à: ", options: ["Análise de compras e consumo trimestral onde calculam lucros prováveis perante grandes sazonalidades", "Representação dos ganhos ou interações ocorridas isoladamente graças ao funcionamento isolado nas vendas publicitárias e subtraindo do número originário de buscas limpas e livres. ", "Soma os acréscimos num volume total num mês na prateleira alheia, transferindo os clientes à lojas digitais regionais concorrente em outros links de forma massificada.", "Expansão imediata orgânica gerando um imposto automático adicional aplicado à vendedores locais perante centros de estoques grátis.  "], correctAnswer: 1, explanation: "No final a Conversão Incremental traduz a pergunta: \"Estes clientes que gastaram online, eles ainda efetuariam suas transações na ausência do Ad publicando o cartaz web?\"", difficulty: "dificil" }
  ]
};
"""
with open(os.path.join(base_dir, "questions.js"), "w") as f:
    f.write(q_js)

# 3. APP.JS
with open(os.path.join(base_dir, "app.js"), "r") as f:
    app_js = f.read()

translations_obj = """
const translations = {
    es: {
        title: "TriviAds",
        subtitle: "Elige tu nivel de dificultad para comenzar el reto.<br/>Tienes 15 segundos por pregunta.",
        facilLabel: "Fácil",
        medioLabel: "Medio",
        altoLabel: "Alto",
        btnFacil: "Nivel Fácil",
        btnMedio: "Nivel Intermedio",
        btnDificil: "Nivel Difícil",
        streak: "Racha",
        question: "Pregunta",
        of: "de",
        points: "Puntos",
        timeout: "¡Se acabó el tiempo! ⏱️",
        correct: "¡Correcto!",
        oops: "¡Oops!",
        continue: "Continuar",
        gameOver: "¡Te quedaste sin vidas! 💔 Repasa e inténtalo de nuevo.",
        master: "¡Impresionante! Has dominado el juego nivel Black. 🚀",
        goodEffort: "¡Muy buen esfuerzo! Completaste el desafío. 💡",
        newRecord: "🎉 ¡Nuevo Récord Personal!",
        review: "📚 Preguntas para repasar:",
        playAgain: "Jugar de Nuevo",
        finalEval: "Evaluación Final",
        pts: "pts",
        q: "P:",
        r: "R:"
    },
    pt: {
        title: "TriviAds",
        subtitle: "Escolha seu nível de dificuldade para começar o desafio.<br/>Você tem 15 segundos por pergunta.",
        facilLabel: "Fácil",
        medioLabel: "Médio",
        altoLabel: "Alto",
        btnFacil: "Nível Fácil",
        btnMedio: "Nível Intermediário",
        btnDificil: "Nível Difícil",
        streak: "Sequência",
        question: "Pergunta",
        of: "de",
        points: "Pontos",
        timeout: "O tempo acabou! ⏱️",
        correct: "Correto!",
        oops: "Ops!",
        continue: "Continuar",
        gameOver: "Você ficou sem vidas! 💔 Revise e tente novamente.",
        master: "Impressionante! Você dominou o jogo nível Black. 🚀",
        goodEffort: "Muito bom esforço! Você completou o desafio. 💡",
        newRecord: "🎉 Novo Recorde Pessoal!",
        review: "📚 Perguntas para revisar:",
        playAgain: "Jogar Novamente",
        finalEval: "Avaliação Final",
        pts: "pts",
        q: "P:",
        r: "R:"
    }
};

window.currentLang = localStorage.getItem('meli_ads_lang') || 'es';

window.setLanguage = function(lang) {
    window.currentLang = lang;
    localStorage.setItem('meli_ads_lang', lang);
    renderStart();
};
"""

app_js = app_js.replace("const app = document.getElementById('app');", "const app = document.getElementById('app');\n" + translations_obj)

# Update texts
app_js = app_js.replace("questions.filter(q => q.difficulty === currentDifficulty);", "questions[window.currentLang].filter(q => q.difficulty === currentDifficulty);")

app_js = app_js.replace("Fácil: <strong>${hsFacil}</strong>", "${translations[window.currentLang].facilLabel}: <strong>${hsFacil}</strong>")
app_js = app_js.replace("Medio: <strong>${hsIntermedio}</strong>", "${translations[window.currentLang].medioLabel}: <strong>${hsIntermedio}</strong>")
app_js = app_js.replace("Alto: <strong>${hsDificil}</strong>", "${translations[window.currentLang].altoLabel}: <strong>${hsDificil}</strong>")

app_js = app_js.replace("<h1>TriviAds</h1>", "<h1>${translations[window.currentLang].title}</h1>")
app_js = app_js.replace("Elige tu nivel de dificultad para comenzar el reto.<br/>Tienes 15 segundos por pregunta.", "${translations[window.currentLang].subtitle}")
app_js = app_js.replace("Nivel Fácil", "${translations[window.currentLang].btnFacil}")
app_js = app_js.replace("Nivel Intermedio", "${translations[window.currentLang].btnMedio}")
app_js = app_js.replace("Nivel Difícil", "${translations[window.currentLang].btnDificil}")

app_js = app_js.replace("🔥 Racha x${streak}", "🔥 ${translations[window.currentLang].streak} x${streak}")
app_js = app_js.replace("Pregunta ${currentQuestionIndex + 1} de ${currentQuestions.length}", "${translations[window.currentLang].question} ${currentQuestionIndex + 1} ${translations[window.currentLang].of} ${currentQuestions.length}")
app_js = app_js.replace("Puntos: ${score}", "${translations[window.currentLang].points}: ${score}")

app_js = app_js.replace("<strong>¡Se acabó el tiempo! ⏱️</strong>", "<strong>${translations[window.currentLang].timeout}</strong>")
app_js = app_js.replace("Continuar", "${translations[window.currentLang].continue}")

app_js = app_js.replace("<strong>${isCorrect ? '¡Correcto!' : '¡Oops!'}</strong>", "<strong>${isCorrect ? translations[window.currentLang].correct : translations[window.currentLang].oops}</strong>")

app_js = app_js.replace("message = \"¡Te quedaste sin vidas! 💔 Repasa e inténtalo de nuevo.\";", "message = translations[window.currentLang].gameOver;")
app_js = app_js.replace("message = \"¡Impresionante! Has dominado el juego nivel Black. 🚀\";", "message = translations[window.currentLang].master;")
app_js = app_js.replace("message = \"¡Muy buen esfuerzo! Completaste el desafío. 💡\";", "message = translations[window.currentLang].goodEffort;")

app_js = app_js.replace("🎉 ¡Nuevo Récord Personal!", "${translations[window.currentLang].newRecord}")
app_js = app_js.replace("📚 Preguntas para repasar:", "${translations[window.currentLang].review}")

app_js = app_js.replace("<strong>P:</strong>", "<strong>${translations[window.currentLang].q}</strong>")
app_js = app_js.replace("<strong>R:</strong>", "<strong>${translations[window.currentLang].r}</strong>")

app_js = app_js.replace("<h1>Evaluación Final</h1>", "<h1>${translations[window.currentLang].finalEval}</h1>")
app_js = app_js.replace("<span style=\"font-size: 1.2rem; color:#888;\">pts</span>", "<span style=\"font-size: 1.2rem; color:#888;\">${translations[window.currentLang].pts}</span>")
app_js = app_js.replace("Jugar de Nuevo", "${translations[window.currentLang].playAgain}")

# Add the language switch to renderStart HTML
switch_html = """
            <div class="lang-switch-container">
                <span class="lang-label ${window.currentLang === 'es' ? 'active' : ''}" onclick="window.setLanguage('es')">ES</span>
                <label class="switch">
                    <input type="checkbox" id="lang-switch" ${window.currentLang === 'pt' ? 'checked' : ''} onchange="window.setLanguage(this.checked ? 'pt' : 'es')">
                    <span class="slider round"></span>
                </label>
                <span class="lang-label ${window.currentLang === 'pt' ? 'active' : ''}" onclick="window.setLanguage('pt')">PT</span>
            </div>
"""
app_js = app_js.replace("<div class=\"card\">", "<div class=\"card\">" + switch_html, 1)

with open(os.path.join(base_dir, "app.js"), "w") as f:
    f.write(app_js)

print("Done patching.")
