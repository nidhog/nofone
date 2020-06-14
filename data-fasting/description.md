# Data Description
This data was captured from `2020-03-01` to `2020-06-01`. During that time, I fasted for 30 days.
* **The period of the fast** from `2020-04-24` to `2020-05-23`
* *The period before the fast* from `2020-03-01` to `2020-04-23`
* *The period after the fast* from `2020-05-24` to `2020-06-01`

**IMPORTANT NOTE**: the period after the fast still contains fasting days and non-fasting days, whereas the period before the fast is mostly non-fasting days.

## The 30 day fast protocol
This fast can be described as a Time Restricted Eating/drinling with an eating/drinking window of 2 hours a day. 

This means:
* around 2 hours of eating/drinking water. The eating window is right after sunset, the exact meal times can be found in `meals.csv`.
* around 22 hours without food or water, each day. Practically, this is between 21 to 23 hours a day. The `trck.csv` file contains the time of the first and last meals as described below.
* for 30 days in the period specified above. 

## Meals `meals.csv`
I logged every meal, with its weight. For some meals, I added an approximation of the calories/macronutrients. I used the Lifesum app to make these approximations.

It contains the following fields:
* `Collection Timestamp` not important. The time when I logged the meal. Do not confuse with the meal time: `Time`.
* `Time` time when I ate the food.
* `Content` Contents of the food separated by newlines (one line for every ingredient).
* `Props` properties of the meal as a comma separated string such as : `Low carb high fat`.
* `Tags` tags for the meal if any as a comma separated string. Such as `breakfast` for the first meal of the day.
* `weight` weight of the meal.
* `comments` comments on the meal, if any.
* `estimated calories` total calories in kCal estimated using the Lifesum app.
* `estimated carb percentage` percentage of carbohydrates estimated using the Lifesum app.
* `estimated fat percentage` percentage of fat estimated using the Lifesum app.
* `estimated protein percentage` percentage of protein estimated using the Lifesum app.

## Exercise `exercise.csv`
I logged every workout session (even if it is as short as 1minute).

It contains the following fields:
* `Collection Timestamp` not important. The time when I logged the exercise. Do not confuse with the time of exercise field `day time`.
* `day time` time when this workout started.
* `type` type of the exercise as a comma separated string (example: `movement, kettlebell`)
* `duration` exercise duration in the format: `HH:MM` (two digits for hours and two digits for minutes)
* `intensity` subjective exercise intensity. From 1 (minimum intensity) to 5 (max intensity).
* `number of reps` integer for the number of repetitions if applicable.
* `comments` comments on the exercise, if any.
* `subjective level` perceived difficulty/level. From 1 (easy) to 5 (hard). This is a subjective measurement.

## Continuous glucose `glucose.csv`
The FreeStyle Libre sensor gives this data, I was wearing different sensors during this period:
* 12 Mar 2020 – 25 Mar 2020
* 26 Mar 2020 – 8 Apr 2020
* 23 Apr 2020 – 6 May 2020
* 7 May 2020 – 20 May 2020
* 21 May 2020 – 3 Jun 2020

The important fields in the glucose are:
* `Device`: same in all the dataset `FreeStyle LibreLink`
* `Serial Number`: same for all rows `b59d4499-1a07-462b-b7da-a179f2093996`
* `Device Timestamp`: time of the glucose measurement (in Stockholm time).
* `Historic Glucose mmol/L`: glucose values in mmol/L.
* `Notes` notes I enter manually, if any.

There are other fields in the data that are not relevant in this case.
## Blood glucose and ketones `gk.csv`
* `Device`: same in all the dataset `FreeStyle LibreLink`
* `Serial Number`: same for all rows `b59d4499-1a07-462b-b7da-a179f2093996`
* `Device Timestamp`: time of the glucose measurement (in Stockholm time).
* `Historic Glucose mmol/L`: glucose values in mmol/L.
* `Notes` notes I enter manually, if any.
## Sleep `sleep.csv`

## Readiness `readiness.csv`

## Weight, eating window and subjective measurements `trck.csv`

## Supplements `supps.csv`

## Habits `hbts.csv`
