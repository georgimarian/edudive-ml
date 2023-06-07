# from sentence_transformers import SentenceTransformer, util
import urllib.request
import PyPDF2
import io 
# import lexrank as lexrank
import re
import pickle

# import numpy as np
# from numpy import dot
# from numpy.linalg import norm

# predef_model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder='./cache')

# # Two lists of sentences
# sentences1 = ["Efficient development of activities organized in a inter-disciplinary group and the development of emphatic abilities of inter-human communication, relationships and collaboration with different groups.",
# "Usage of efficient learning, information, research and development methods and techniques for knowledge revaluation abilities, for adaptation to the requirements of a dynamic society, and for communication in romanian language and another foreign language.",
# "Team work capabilities; able to fulfill different roles",
# "Professional communication skills; concise and precise description, both oral and written, of professional results",
# "Antrepreneurial skills;"]

# sentences2 = ['Teamwork, cooperation, collaboration',
#               'Adapting, researching, eliciting requirements',
#               'Teamwork, coordination, leadership',
#               'Communication, summarization',
#               'Antrepreneurship']

# #Compute embedding for both lists
# embeddings1 = model.encode(sentences1, convert_to_tensor=True)
# embeddings2 = model.encode(sentences2, convert_to_tensor=True)

# #Compute cosine-similarities
# cosine_scores = util.cos_sim(embeddings1, embeddings2)

# #Output the pairs with their score
# for i in range(len(sentences1)):
#     print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i]))
# def cos_sim(a, b):
#   a = np.array(a)
#   b = np.array(b)
#   return dot(a, b)/(norm(a)*norm(b))

predef_model = ''
def document_process(model = predef_model, cos_sim=''): 
  print(model)
  if model == predef_model:
    pickle.dump(predef_model, open('saved_model.pkl', 'wb'))
    # pickle.dump(util.cos_sim, open('cos_sim.pkl','wb'))
  cos_sim = pickle.load(open('cos_sim.pkl', 'rb'))
  URLS = [
    'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem1_MME8025_en_grigo_2022_6966.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem1_MME8005_en_vladi_2022_6967.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem1_MME8028_en_craciunf_2022_7328.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem1_MME8143_en_dsuciu_2022_7099.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem1_MMR9001_ro_bparv_2022_6989.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem1_FEUM0202_en_dana_2022_7492.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem2_MME8024_en_adriana_2022_6706.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem2_MME8023_en_motogna_2022_6764.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem2_MME8022_en_craciunf_2022_6823.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem2_MME8065_en_arthur_2022_7449.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem2_MME8051_en_ilazar_2022_6968.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem2_MME8059_en_mihai-suciu_2022_7388.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem2_MME8190_en_avescan_2022_7418.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem2_MMR8087_ro_sabina_2022_7159.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem3_MME8026_en_avescan_2022_7126.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem3_MME8027_en_ilazar_2022_6897.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem3_MME8150_en_avescan_2022_6738.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem3_MME8158_en_oana_2022_7061.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem3_MME8148_en__2022_7333.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem3_MME8063_en_istvanc_2022_6700.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem3_MME8048_en_hfpop_2022_7064.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem3_MLE8009_en_rgaceanu_2022_7362.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem3_MMR8159_ro_lauras_2022_7013.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem4_MME3042_en_motogna_2022_7010.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem4_MME9009_en_motogna_2022_6763.pdf',
    # 'https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem4_MME9012_en_motogna_2022_7073.pdf',
  ];

  #create an empty dictionary 
  file_dict = {} 

  #loop through the lines in the text file 
  # key = 0; 
  for URL in URLS: 
    req = urllib.request.Request(URL)
    remote_file = urllib.request.urlopen(req).read()
    remote_file_bytes = io.BytesIO(remote_file)
    pdfdoc_remote = PyPDF2.PdfReader(remote_file_bytes)
    raw = pdfdoc_remote.pages[1].extract_text()
    # print(pdfdoc_remote.pages[1].extract_text())
    # print(raw)
    textParsed = raw.replace('\n', '')

    # print('------------' )

    cp_key = 'Professional competencies' if len(textParsed.split('Professional competencies')) > 1 else 'Competenţe profesionale'
    tp_key = 'Transversal competencies' if len(textParsed.split('Transversal competencies')) > 1 else 'Competenţe transversale'
    gobj_key = 'General objective of the discipline' if len(textParsed.split('General objective of the discipline')) > 1 else 'Obiectivul general al disciplinei'
    sobj_key = 'Specific objective of the discipline' if len(textParsed.split('Specific objective of the discipline')) > 1 else 'Obiectivele specifice'
    file_dict[URL.split('https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/')[1]] = {
        'pc': ''.join(re.sub('(C\d*\.*\d*)', '\n', textParsed.split(cp_key)[1].split('Transversal competencies')[0].strip())),
        'tc': re.sub('(CT\d*\.*\d*)', '\n',textParsed.split(tp_key)[1].split('General objective of the discipline')[0].strip()),
        'gobj': textParsed.split(gobj_key)[1].split('Specific objective of the discipline')[0].strip(),
        'sobj': textParsed.split('Specific objective of the discipline')[1].split('Course')[0].strip()
    }
    print('~~~~~~~~~~' )

    for subject in file_dict:
      for competency in file_dict[subject]: 
        for elem in file_dict[subject][competency].split('·'):
          print(elem)
        # for entry in file_dict[subject][competency]:
        #   print("rve")
        #   print(entry)
          # entry = entry.split('·')
    # #split the line on ':' 
    # if re.search("[0-9]*\.[0-9]", line):
    #   value = line
    # #strip the whitespace 
    # key = key+1
    # value = value.strip() 
    # #add the key, value pair to the dictionary 
    # file_dict[key] = value 
    
  #print the dictionary 
  # print('----------------')

  # print(file_dict)

  # embedder = SentenceTransformer('distiluse-base-multilingual-cased-v2')
  skills = [
        'Agile methodologies', 
        'Agile practices', 
        'Communication', 
        'Activitati de cercetare', 
        'Etica'
        ]
  
  result = []

  for entry in file_dict:
    print(entry) 
    for elem in file_dict[entry]:
      print(elem + ': ' + file_dict[entry][elem])
      elements = [None] * 10
      for i in range(len(elements)):
        elements[i] = file_dict[entry][elem]
      # embeddings1 = embedder.encode(elements, convert_to_tensor=True)
      # embeddings2 = embedder.encode(skills, convert_to_tensor=True)
      embeddings1 = model.encode(elements, convert_to_tensor=True)
      embeddings2 = model.encode(skills, convert_to_tensor=True)

      cosine_scores = cos_sim(embeddings1, embeddings2)


      #Output the pairs with their score
      for i in range(len(skills)):
          # print("{} \t\t {} \t\t Score: {:.4f}".format(elements[i], skills[i], cosine_scores[i][i]))
          result.append({'element': elements[i], 'skill': skills[i], 'score': cosine_scores[i][i].item()})

    # print('\n') 

    # print('+++++++++++++++++++++')

  
  return result
#   Multilingual

# # distiluse-base-multilingual-cased-v2
# embedder = SentenceTransformer('distiluse-base-multilingual-cased-v2')
# s1 = ['Identification and understanding of basic concepts of the following specific Agile methodologies: Scrum, Extreme Programing, Kanban, Lean Software Development',
#       'Identification and explanation of basic Agile practices',
#  'Formal communication in organizations - Project task time and effort estimation - Change management',
#  'înțelegerea conceptelor, metodelor și modelelor folosite în activitățile de cercetare • înțelegerea principiilor proiectării și realizării diverselor activități de cercetare • inițierea în cercetarea științifică de informatică Competenţe transversale', 
#  'abilitatea de a recenza o lucrare științifică',
#  'abilitatea de a efectua muncă eficientă și riguroasă de cercetare',  
#  'manifestarea unei atitudini proactive și eficace în procesul de cercetare', 
#  'manifestarea unei atitudini proactive și eficace în procesul de cercetare • respectarea principiilor de etică și deontologie profesională  ']
# s2 = ['Agile methodologies', 
#       'Agile practices', 
#       'Communication', 
#       'Activitati de cercetare', 'Etica']
# embeddings1 = embedder.encode(s1, convert_to_tensor=True)
# embeddings2 = embedder.encode(s2, convert_to_tensor=True)

# cosine_scores = util.cos_sim(embeddings1, embeddings2)


# #Output the pairs with their score
# for i in range(len(s2)):
#     print("{} \t\t {} \t\t Score: {:.4f}".format(s1[i], s2[i], cosine_scores[i][i]))

# """
# This example uses LexRank (https://www.aaai.org/Papers/JAIR/Vol22/JAIR-2214.pdf)
# to create an extractive summarization of a long document.

# The document is splitted into sentences using NLTK, then the sentence embeddings are computed. We
# then compute the cosine-similarity across all possible sentence pairs.

# We then use LexRank to find the most central sentences in the document, which form our summary.

# Input document: First section from the English Wikipedia Section
# Output summary:
# Located at the southern tip of the U.S. state of New York, the city is the center of the New York metropolitan area, the largest metropolitan area in the world by urban landmass.
# New York City (NYC), often called simply New York, is the most populous city in the United States.
# Anchored by Wall Street in the Financial District of Lower Manhattan, New York City has been called both the world's leading financial center and the most financially powerful city in the world, and is home to the world's two largest stock exchanges by total market capitalization, the New York Stock Exchange and NASDAQ.
# New York City has been described as the cultural, financial, and media capital of the world, significantly influencing commerce, entertainment, research, technology, education, politics, tourism, art, fashion, and sports.
# If the New York metropolitan area were a sovereign state, it would have the eighth-largest economy in the world.
# """



# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Our input document we want to summarize
# # As example, we take the first section from Wikipedia
# document = """
# As for the future, I plan to develop my Software Engineer career by studying at a Software Engineering Master’s program in Computer Science, learning about technologies and methodologies at the highest level. 
# Software Engineering is strongly coupled with the developer career, and I believe such a Master would aid me in becoming a better developer for the following two years..
# I would like to apply the gained knowledge in the context of a Distributed Web and Mobile application, having both microservices on the back-end and micro-frontend architectures on the front-end. 
# The proposed application domain is that of an Erasmus application/management tool, in which students’ access to Erasmus+ scholarships is facilitated.
# Such an application would enable me to strengthen my backend and mobile skills, while also researching the domain of micro-frontends.
# Upon finishing my Master’s degree, I would like to further my career in Computer Science by aiming to become a Software Architect in a company, while also applying for a PhD in a related field. 
# I would like for my education to strongly support my professional development and to make me a better programmer and leader. 
# If possible, I would like to offer my knowledge in teaching other young students how to better themselves as coders and to learn from all the mistakes I have made during my career path. 
# I believe that my professional and academic performance, together with my Erasmus experience, would help me bring innovation as a teacher and make Computer Science more attractive to students.
# """

# #Split the document into sentences
# sentences = nltk.sent_tokenize(document)
# print("Num sentences:", len(sentences))

# #Compute the sentence embeddings
# embeddings = model.encode(sentences, convert_to_tensor=True)

# #Compute the pair-wise cosine similarities
# cos_scores = util.cos_sim(embeddings, embeddings).numpy()

# #Compute the centrality for each sentence
# centrality_scores = degree_centrality_scores(cos_scores, threshold=None)

# #We argsort so that the first element is the sentence with the highest score
# most_central_sentence_indices = np.argsort(-centrality_scores)


# #Print the 5 sentences with the highest scores
# print("\n\nSummary:")
# for idx in most_central_sentence_indices[0:5]:
#     print(sentences[idx].strip())
