article = """

CNN - President Joe Biden on Wednesday asked if a congresswoman who died last month was present at a White House food insecurity conference.At the event, the White House’s first hunger conference since 1969, Biden took a moment during his remarks to credit a list of bipartisan elected officials. All of the officials he listed were behind a bill establishing Wednesday’s conference, and the late Indiana Republican Rep. Jackie Walorski was a co-sponsor. “I want to thank all of you here for including bipartisan elected officials like Rep. (Jim) McGovern, Sen. (Mike) Braun, Sen. (Cory) Booker, Representative – Jackie, are you here? Where’s Jackie? I think she wasn’t going to be here – to help make this a reality,” Biden said." 

Walorski, who was 58, died last month in a car accident that also killed two of her staffers. She began serving in Congress in 2013. Before her death, the congresswoman was the co-chair of the House Hunger Caucus.

When asked by reporters about the comment later on Wednesday, White House press secretary Karine Jean-Pierre said Biden was, in fact, referencing Walorski.

“The President was naming the congressional champions on this issue and was acknowledging her incredible work. He had already planned to welcome the congresswoman’s family to the White House on Friday. There will be a bill signing in her honor this coming Friday, so, of course, she was on his mind,” Jean-Pierre said. “She was top of mind for the President. He very much looks forward to discussing her remarkable legacy of public service with them when he sees her family this coming Friday.”

Biden had issued a statement upon her death, saying that both he and first lady Dr. Jill Biden were “shocked and saddened” by her passing. The White House also flew flags at half-staff in honor of her death.

“We may have represented different parties and disagreed on many issues, but she was respected by members of both parties for her work on the House Ways and Means Committee on which she served,” Biden’s statement last month said. “She also served as co-chair of the House Hunger Caucus, and my team and I appreciated her partnership as we plan for a historic White House Conference on Hunger, Nutrition, and Health this fall that will be marked by her deep care for the needs of rural America.”

At the end of a panel later during Wednesday’s hunger conference, White House Domestic Policy Council Director Susan Rice mentioned Walorski and the rest of the congressional group responsible for facilitating the conference.

“Well, all right everybody, please join me in thanking Sens. Booker and Braun, Chairman McGovern and the late Jackie Walorski for her extraordinary leadership to make this possible. We would not be here without them,” she said.
"""

substitutions = {
  "Joe Biden": "Sleepy Joe",
  "Biden": "Brandon",
  "Biden's": "Brandon's",
  "White House": "Pit of Heresy",
  "America": "Hell on Earth",
}

for key, value in substitutions.items():
  article = article.replace(key, value)

print(article)