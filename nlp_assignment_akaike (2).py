# -*- coding: utf-8 -*-
"""NLP_Assignment.Akaike.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jc-tpX89IChOO0Et7b0dqciT4SJGbFbd

# **Genrating MultipleChoose Q&A Using NLP(Spacy)**

# **Imported Libraries**
"""

import spacy
import random
import os

"""# **Spacy Loaded For English Language**"""

nlp=spacy.load("en_core_web_sm")

"""# **Function for Context & Questions Genration**"""

def get_mca_questions(context:str,num_questions:int):
  doc=nlp(context)

"""# **Function for Genrating MCQs**"""

def get_mcq_multicorrect_ans(Questions,Correct_Answers,Wrong_Options,num_options=4):
  options=Correct_Answers+Wrong_Options
  random.shuffle(options)
  mcq = {
      "question" : question,
      "options" : options,
      "Correct_Answers" : Correct_Answers

  }

"""# **Function Block for Genrating Different MCQs**"""

def get_different_questions():

  sentence=random.choice(list(doc.sents)) # Select Sentence from context
  non_pronounciation_words = random.choice([token for token in sentence if not token.is_punct]) # Selecting non_pronounciation words or meaningless words
  Questions = sentence.text.replace(non_pronounciation_words,"_______")# creating questions with blank word
  Correct_Answers =[non_pronounciation_words.text] # Assigning Correct answers to meaningless words
  Wrong_options=[token.text for token in doc if token.is_alpha and token.text!=Correct_Answers[0]]#probablity of answers other than correct answers
  num_correct_answers=random.randint(1,2)#Mention how many correct answers using rand
  Correct_Answers.extend=(random.sample(Wrong_options,num_correct_answers))
  num_other_options=min(4- num_correct_answers,len(Wrong_options))
  Wrong_options=random.sample(Wrong_options,num_other_options)
  mcq=get_mcq_multicorrect_ans(Questions,Correct_Answers,Wrong_options)
  return mcq

"""# **Loops For Genrating Questions and Choices**"""

questions=[get_different_questions() for _ in range(num_questions)]
MCA_Questions=[]
for i,question in enumerate(questions,start=1):
  question_str=f"Q{i}:{questions['questions']}\n"
  option_str = ""
  for j,option in enumerate(question['options']):
    option_str += f"{j+1}.{option}.\n"
    converted_answers="&".join([f"({chr(97+question['options'].index(ans))})"for ans in question["correct_answers"]])
    correct_options_str=f"Correct Options: {converted_answers}\n"
    MCA_Question=f"{question_str}{option_str}{correct_options_str}\n"
    MCA_Questions.append(MCA_Question)
#return MCA_Questions

"""# **Inputs & Questions Display**"""

context = input("Insert any Paragraph : " )
num_questions = int(input("Number of MCQ :"))
MCA_Questions= get_mca_questions(context,num_questions)
for question in MCA_Questions:
  print(question)

"""# **Output Execution Block**"""

def get_mca_questions(context:str,num_questions:int):
  doc=nlp(context)

  def get_mcq_multicorrect_ans(question,Correct_Answers,Wrong_Options,num_options=4):
      options=Correct_Answers+Wrong_Options
      random.shuffle(options)
      mcq = {
      "question" : question,
      "options" : options,
      "Correct_Answers" : Correct_Answers
     }
      return mcq

  def get_different_questions():
         sentence=random.choice(list(doc.sents)) # Select Sentence from context
         non_pronounciation_words = random.choice([token for token in sentence if not token.is_punct]) # Selecting non_pronounciation words or meaningless words
         Questions_Text = sentence.text.replace(non_pronounciation_words.text,"_______")# creating questions with blank word
         Correct_Answers =[non_pronounciation_words.text] # Assigning Correct answers to meaningless words
         Wrong_options=[token.text for token in doc if token.is_alpha and token.text!=Correct_Answers[0]]#probablity of answers other than correct answers
         num_correct_answers=random.randint(1,2)#Mention how many correct answers using rand
         Correct_Answers.extend(random.sample(Wrong_options,num_correct_answers))
         num_other_options = min(4 - num_correct_answers,len(Wrong_options))
         Wrong_options=random.sample(Wrong_options,num_other_options)
         mcq=get_mcq_multicorrect_ans(Questions_Text,Correct_Answers,Wrong_options)
         return mcq
  questions = [get_different_questions() for _ in range(num_questions)]
  MCA_Questions=[]
  for i,question in enumerate(questions,start=1):
          question_str = f"Q{i}: {question['question']}\n"
          #question_str = f"Q{i}: {question['question']}\n"
          option_str = ""

          for j,option in enumerate(question['options']):
              option_str += f"{j+1}.{option}\n"

          converted_answers =" & ".join([f"({chr(97+question['options'].index(ans))})" for ans in question["Correct_Answers"]])
          correct_options_str=f"Correct Options: {converted_answers}\n"

          MCA_Question=f"{question_str}{option_str}{correct_options_str}\n"
          MCA_Questions.append(MCA_Question)

  return MCA_Questions
context = input("Insert any Paragraph : " )
num_questions = int(input("Number of MCQ :"))
MCA_Questions= get_mca_questions(context,num_questions)
for question in MCA_Questions:
   print(question)