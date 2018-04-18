######################################################################
#  CC0 1.0 Universal
#  $Author: celsa diaz tejada
#  $Date: 10/11/15
#  $Name: eQuiz Test your german vocabulary knowledge ;)
######################################################################

import numpy as np
import pandas as pd
import argparse


class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()  
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)

def transform_and_suffle_namen_split_input(data, num_samples):
    # transform splitted namen input data
    die = data.loc[:, ['eKuche', 'Unnamed: 1']].rename(columns={'eKuche': 'name', 'Unnamed: 1': 'meaning'})
    der = data.loc[:, ['rBalkon', 'Unnamed: 3']].rename(columns={'rBalkon': 'name', 'Unnamed: 3': 'meaning'})
    das = data.loc[:, ['sZimmer', 'Unnamed: 5']].rename(columns={'sZimmer': 'name', 'Unnamed: 5': 'meaning'})
    die.loc[:, 'gender'] = 'die'
    der.loc[:, 'gender'] = 'der'
    das.loc[:, 'gender'] = 'das'
    df_restructured = pd.concat([die, der, das], axis=0).dropna()

    # select and suffle input data
    selection = df_restructured.index.tolist()
    np.random.shuffle(selection)
    selection = selection[:num_samples]

    return df_restructured.loc[selection, :]


def transform_and_suffle_namen_wo_split_input(data, num_samples):
    # transform namen input data
    data['gender'] = data['Namen'].str.split(' ').apply(lambda x: "".join(x[0]))
    data['name'] = data['Namen'].str.split(' ').apply(lambda x: " ".join(x[1:]))
    data['gender'] = data['gender'].replace('e', 'die').replace('r', 'der').replace('s', 'das')
    df_restructured = data.drop(['Namen'], axis=1)

    # select and suffle input data
    np.random.seed(0)
    selection = df_restructured.index.tolist()
    np.random.shuffle(selection)
    selection = selection[:num_samples]

    return df_restructured.loc[selection, :]


def transform_and_suffle_verben_akk_dat_input(data, num_samples):
    # transform splitted namen input data
    akk = data.loc[:, ['Akkusative', 'Unnamed: 1']].rename(columns={'Akkusative': 'verb', 'Unnamed: 1': 'meaning'})
    dat = data.loc[:, ['Dativ', 'Unnamed: 3']].rename(columns={'Dativ': 'verb', 'Unnamed: 3': 'meaning'})
    akk.loc[:, 'object'] = 'akk'
    dat.loc[:, 'object'] = 'dat'
    df_restructured = pd.concat([akk, dat], axis=0).dropna()

    # select and suffle input data
    selection = df_restructured.index.tolist()
    np.random.shuffle(selection)
    selection = selection[:num_samples]

    return df_restructured.loc[selection, :]


def transform_and_suffle_starken_verben_input(data, num_samples):
    # transform splitted namen input data
    inf = data.loc[:, ['Infinitiv + Ergänzung', 'meaning']].rename(columns={'Infinitiv + Ergänzung': 'konjugation'})
    pres = data.loc[:, ['3. Person Präsens', 'meaning']].rename(columns={'3. Person Präsens': 'konjugation'})
    prae = data.loc[:, ['3. Person Präteritum', 'meaning']].rename(columns={'3. Person Präteritum': 'konjugation'})
    part = data.loc[:, ['Hilfsverb + Partizip II', 'meaning']].rename(
        columns={'Hilfsverb + Partizip II': 'konjugation'})
    inf.loc[:, 'zeit'] = 'infinitiv'
    pres.loc[:, 'zeit'] = '3_person_present'
    prae.loc[:, 'zeit'] = '3_person_praeter'
    part.loc[:, 'zeit'] = 'partII'
    df_restructured = pd.concat([inf, pres, prae, part], axis=0).dropna()

    # select and suffle input data
    selection = df_restructured.index.tolist()
    np.random.shuffle(selection)
    selection = selection[:num_samples]

    return df_restructured.loc[selection, :]


def transform_and_suffle_wortschatz_input(data, num_samples):
    # transform splitted namen input data
    columns = data.columns.tolist()
    df_restructured = data.rename(columns={columns[0]: 'wort', columns[1]: 'meaning'})

    # select and suffle input data
    selection = df_restructured.index.tolist()
    np.random.shuffle(selection)
    selection = selection[:num_samples]

    return df_restructured.loc[selection, :]


def evaluate_user_answer_namen(row):
    translation = input("How do you say {} in german? ".format(row['meaning']))
    gender = input("What is the gender of {}? ".format(row['meaning']))
    if translation == row['name'] and gender == row['gender']:
        print("You were correct!")
        answer = True
    else:
        print("You are wrong, the translation is {} and the gender is {}.".format(row['name'], row['gender']))
        answer = False
    return answer


def evaluate_user_answer_verben_akk_dat(row):
    translation = input("How do you say {} in german? ".format(row['meaning']))
    object_type = input("Which is the type of object with the verb {}? akk or dat? ".format(row['meaning']))
    if translation == row['verb'] and object_type == row['object']:
        print("You were correct!")
        answer = True
    else:
        print("You are wrong, the translation is {} and the object type is {}.".format(row['verb'], row['object']))
        answer = False
    return answer


def evaluate_user_answer_starken_verben(row):
    translation = input("How is the {} of the verb \"{}\" in german? ".format(row['zeit'], row['meaning']))
    if translation == row['konjugation']:
        print("You were correct!")
        answer = True
    else:
        print("You are wrong, the translation is {} and the time is {}.".format(row['zeit'], row['konjugation']))
        answer = False
    return answer


def evaluate_user_answer_wortschatz(row):
    translation = input("How do you say \"{}\" in german? ".format(row['meaning']))
    if translation == row['wort']:
        print("You were correct!")
        answer = True
    else:
        print("You are wrong, the translation is {}.".format(row['wort']))
        answer = False
    return answer


def main():
    parser = argparse.ArgumentParser(description="Test your german knowledge.", usage="\nUsage for quiz of names splitted by gender:\npython eQuiz.py -t namen_split -i path_to_your_csv.csv -n num_exercises\n\nUsage for quiz of names without splitting by gender:\npython eQuiz.py -t namen_wo_split -i path_to_your_csv.csv -n num_exercises\n\nUsage for quiz of verbs splitting by akusative or dative:\npython eQuiz.py -t verben_akk_dat -i path_to_your_csv.csv -n num_exercises\n\nUsage for quiz of verbs declination:\npython eQuiz.py -t verben_deklination -i path_to_your_csv.csv -n num_exercises\n\nUsage for quiz of simply vocabulary:\npython eQuiz.py -t wortschatz -i path_to_your_csv.csv -n num_exercises.", formatter_class=SmartFormatter)

    parser.add_argument('--task', choices=['namen_split', 'namen_wo_split', 'verben_akk_dat', 'verben_deklination',
                                           'wortschatz'])
    parser.add_argument('--input', help='./data/wortschatz.csv')
    parser.add_argument('--num', help='Number of elements in the quiz to test.')

    args = parser.parse_args()

    if args.task == 'namen_split':
        df_selection = transform_and_suffle_namen_split_input(args.input, args.num)
        results = df_selection.apply(lambda x: evaluate_user_answer_namen(x), axis=1)

    if args.task == 'namen_wo_split':
        df_selection = transform_and_suffle_namen_wo_split_input(args.input, args.num)
        results = df_selection.apply(lambda x: evaluate_user_answer_namen(x), axis=1)

    if args.task == 'verben_akk_dat':
        df_selection = transform_and_suffle_verben_akk_dat_input(args.input, args.num)
        results = df_selection.apply(lambda x: evaluate_user_answer_verben_akk_dat(x), axis=1)

    if args.task == 'verben_deklination':
        df_selection = transform_and_suffle_starken_verben_input(args.input, args.num)
        results = df_selection.apply(lambda x: evaluate_user_answer_starken_verben(x), axis=1)

    if args.task == 'wortschatz':
        df_selection = transform_and_suffle_wortschatz_input(args.input, args.num)
        results = df_selection.apply(lambda x: evaluate_user_answer_wortschatz(x), axis=1)

    print(
        "You answer {} times correctly.\nThe percentage of correct answers is {}.".format(sum(results),
                                                                                          sum(results) * 100 / args.num))


if __name__ == "__main__":
    main()
