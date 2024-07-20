# import os
# from nltk import word_tokenize
# from sample_code_1 import num_sentences, spelling_mistakes
# from sample_code_2 import agreement, verb


# def load_essay(essay_filename):
#     with open(essay_filename, 'r') as file:
#         return file.read()


# def score_essay(essay_text):
#     num_sent = num_sentences(essay_text)  # sentences and words (a)
#     spell_errors = spelling_mistakes(essay_text)  # spelling errors (b)
#     tokens = word_tokenize(essay_text)
#     agreement_errors = agreement(tokens)  # agreement errors (c.i)
#     verb_errors = verb(tokens)  # verb errors (c.ii)
#     print(f"Number of sentences: {num_sent}")
#     print(f"Spelling mistakes: {spell_errors}")
#     print(f"Errors on agreement: {agreement_errors}")
#     print(f"Errors on verb: {verb_errors}")
#     return num_sent, spell_errors, agreement_errors, verb_errors


# # this function is for making our scale. we calculated the averages, and denoted the average to be a 3 on the range
# def calculate_score(scores):

#     average_num_sent = sum(x[0] for x in scores) / len(scores)
#     average_spell_errors = sum(x[1] for x in scores) / len(scores)
#     average_agreement_errors = sum(x[2] for x in scores) / len(scores)
#     average_verb_errors = sum(x[3] for x in scores) / len(scores)
#     # Overall scores: (14.48, 11.37, 22.75, 12.38)
#     return average_num_sent, average_spell_errors, average_agreement_errors, average_verb_errors


# def calculate_formula(scaled_scores):
#     a, b, c, d = scaled_scores
#     return 2 * a - b + c + d


# def calculate_range(essay_scores, averages):
#     num_sent, spell_errors, agreement_errors, verb_errors = essay_scores
#     avg_sentences, avg_spelling, avg_agreement, avg_verb = averages

#     # Function to calculate score for sentences, unique because a score of 10 should award the max.
#     def score_sentences(sentences):
#         if sentences >= 10:
#             return 5
#         else:
#             return max(1, int(5 * (sentences / 10)))

#     def score_spelling_errors(spelling):
#         # This is unique for spelling errors: higher errors means higher score (such that 2a - b is preserved)
#         if spelling >= 16:
#             return 4
#         elif spelling >= 14:
#             return 3
#         elif spelling >= 11:
#             return 2
#         elif spelling >= 9:
#             return 1
#         else:
#             return 0

#     # This is fine for 3rd and 4th scores
#     def score_errors(actual, average):
#         if actual <= average:
#             return min(5, 3 + ((average - actual) // 2))
#         else:
#             return max(1, 3 - ((actual - average) // 2))

#     scaled_sentence = score_sentences(num_sent)
#     scaled_spelling = score_spelling_errors(spell_errors)
#     scaled_agreement = score_errors(agreement_errors, avg_agreement)
#     scaled_verb = score_errors(verb_errors, avg_verb)

#     return scaled_sentence, scaled_spelling, scaled_agreement, scaled_verb


# def main():
#     essays_dir = 'essays'
#     averages = (14, 11, 22, 12)  # averages if you were to run all of them at once and comment the "yes" block
#     # see below for that (this one was hardcoded to not have to iterate the whole folder)
#     all_scores = []
#     try:
#         files = os.listdir(essays_dir)
#         for filename in files:
#             full_path = os.path.join(essays_dir, filename)
#             essay_text = load_essay(full_path)
#             print(f"\nGrading {filename}:")
#             essay_scores = score_essay(essay_text)
#             all_scores.append(essay_scores)
#             scaled_scores = calculate_range(essay_scores, averages)
#             print("Scaled scores:", scaled_scores)

#             final_score = calculate_formula(scaled_scores)
#             print(f"Final score for {filename}: {final_score}")
#             # comment this block until the "end comment block" line to see the full averages
#             user_input = input("Do you want to continue with the next file? (y/n): ")
#             if user_input.lower() != 'y':
#                 break
#             # end comment block
#             print('---' * 20)
#             overall_scores = calculate_score(all_scores)
#             # NOTE: THESE ARE NOT RANGES. They are averages that were used in the
#             #  calculation of the ranges, see (calculate_range())
#             print(f"Overall averages: {overall_scores}")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     main()
