#...

school = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores': [5,3,5,5,5]}, {'school_class': '4v', 'scores': [1,5,5,2,3]}]
marks_av = []
for sch_class in school: #sch_class принимает последовательно значения в виде словарей списка
	av_mark = sum(sch_class.get("scores")) / len(sch_class.get("scores")) #узнаем среднюю оценку по классу
	print('Средняя оценка по классу {} равна {}'.format(sch_class.get("school_class"), av_mark))
	marks_av.append(av_mark)
print('Средняя оценка по школе — {}'.format(sum(marks_av) / len(marks_av)))

#print("\n".join(["Средняя оценка по классу {} равна {}".format(name,score) for score,name in zip([sum(x['scores']) / len(x['scores']) for x in school],[x['school_class'] for x in school])]))
#print("Средняя оценка по школе {}".format(sum([sum(x['scores']) for x in school]) / sum([len(x['scores']) for x in school])))