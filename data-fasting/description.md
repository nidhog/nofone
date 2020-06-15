# Data Description
This data was captured from `2020-03-01` to `2020-06-01`. During that time, I fasted for 30 days.
* **The period of the fast** from `2020-04-24` to `2020-05-23`
* *The period before the fast* from `2020-03-01` to `2020-04-23`
* *The period after the fast* from `2020-05-24` to `2020-06-01` (includes fasting days and non-fasting days)

To find fasting days in the data: every fasting day has the tag `fast` in the `trck.csv` file. Every fasting day also corresponds to a value `YES` for the field `fast` in the `hbts.csv` file.

## What type of fast it was
This fast can be described as a Time Restricted Eating/drinling with an eating/drinking window of 2 hours a day. 

This means:
* for 30 days from `2020-04-24` to `2020-05-23`. 
* around 22 hours without food or water, each day. 
* around 2 hours of eating/drinking water. The eating window is right after sunset, the exact meal times can be found in `meals.csv`.

Practically, for every fasting day is between 21 to 23 hours a day. The `trck.csv` file contains the time of the first and last meals as described below.

This fast was during the month of ramadan which is why the `ramadan` tag in `trck.csv` points to this period.

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
* `estimated calories` total calories in kCal estimated using the Lifesum app. Only collected in a few days.
* `estimated carb percentage` percentage of carbohydrates estimated using the Lifesum app. Only collected in a few days.
* `estimated fat percentage` percentage of fat estimated using the Lifesum app. Only collected in a few days.
* `estimated protein percentage` percentage of protein estimated using the Lifesum app. Only collected in a few days.

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
The FreeStyle Libre sensor gives this data as a csv file. I was wearing a different sensor for every one of these periods:
* 17 Mar 2020 – 31 Mar 2020
* 24 Apr 2020 –  8 May 2020
*  8 May 2020 –  19 May 2020
* 19 May 2020 – 2 Jun 2020

The important fields in the here are:
* `Device`: same in all the dataset `FreeStyle LibreLink`
* `Serial Number`: same for all rows `b59d4499-1a07-462b-b7da-a179f2093996`
* `Device Timestamp`: time of the glucose measurement (in Stockholm time).
* `Historic Glucose mmol/L`: glucose values in mmol/L.
* `Notes` notes I enter manually, if any.

There are other fields in the data that are not relevant in this case.
## Blood glucose and ketones `gk.csv`
I collected these measures of sugar and fats in the blood (glucose and ketones) using the KetoMojo device (by finger pricking).

It contains the following fields:
* `Collection Timestamp` not important. The time when I logged the measurement on the data sheet. Do not confuse with the time where the blood sample was taken: `time`.
* `time` time when I collected the blood glucose and ketone measurement (in GMT+1).
* `glucose` glucose level in the blood in mg/dL.
* `glucose (mmol/L)` glucose level in the blood in mmol/L.
* `ketones`  level of ketones in the blood in mmol/L.
* `gki`  glucose ketone index (level og glucose divided by the level of ketones, both in mmol/L).
* `hct` estimated hematocrit.
* `hb` estimated hemoglobin.
* `hours since last meal` hours from the time I stopped eating to the time I took the measurement.
* `comments` comments on the measurement, if any.
* `tags` tags as a comma separated value string, contains tags such as `morning` for morning measurements, `exercise` if I worked out close to the measurement.
## Sleep `sleep.csv`
Sleep measurements as measured by the Oura ring device.

Each row gives a measurement for one night of sleep. The index for the day before that night of sleep is given as:
* `summary_date` in the format: `YYYY-MM-DD`. So this is not to be confused with the day after the night of sleep.

These include the estimated sleep time fields:
* `total` total amount of sleep in seconds. 
* `deep` total amount of deep sleep in seconds.
* `rem` total amount of rapid-eye-movement sleep in seconds.
* `light` total amount of light sleep in seconds.

Note that `total`=`deep`+`rem`+`light` as defined below.

This data also includes heart-rate related measurements such as:
* `hr_average` average Heart Rate.
* `hr_lowest` lowest Heart Rate during the night.
* `rmssd` Heart Rate Variability averaged using the rmssd method.

There are a lot of other fields included such as the start of the bedtime and the end of the bedtime. [The Oura ring's official documentation explains these fields in detail here: https://cloud.ouraring.com/docs/sleep](https://cloud.ouraring.com/docs/sleep)

## Readiness `readiness.csv`
Oura defines Readiness as: how ready you are for the day. It uses multiple measurements to compute scores for readiness.
[The Oura ring's official documentation explains these fields in detail here: https://cloud.ouraring.com/docs/readiness](https://cloud.ouraring.com/docs/readiness)

## Weight, eating window and subjective measurements `trck.csv`
This data includes weight, eating window and some subjective measurements (such as sleep and productivity).

* `DAY` the day that these measurements are referring to in the format: `MM/DD/YYYY`.
* `WEIGHT (kg)` the weight in kg. Measured every morning on the same scale.
* `BREAK FAST TIME` first meal of the day. In the format HH:MM, in UTC.
* `BREAK WATER-FAST TIME` first water drink of the day. In the format HH:MM, in UTC.
* `LATEST MEAL TIME` the time I stopped eating. In the format HH:MM, in UTC.
* `WORK` whether I worked from home `wfh`, from stockholm `stockholm` or did not work `none`.
* `SLEEP (SUBJECTIVE)` a subjective sleep measurement. How I perceived my sleep from the night before. From 1 (not good sleep) to 10 (great sleep). This measurement skips the value 7.
* `PRODUCTIVITY (SUBJECTIVE)` subjective productivity measurement from 1 (not productive) to 10 (very productive). This measurement skips the value 7.
* `energy level subjective` subjective energy level measurement from 1 (no energy) to 10 (lots of energy). This measurement skips the value 7.
* `TAGS` tags as comma separated values. These can include `fast` for fasting days and `CGM` for days where I was wearing a continuous glucose monitor etc.

## Supplements `supps.csv`
These fields specify whether I took certain supplements. For some of these supplements, the field contains the exact amount I took.

* `DAY` the day that these measurements are referring to in the format: `MM/DD/YYYY`.
* `chlorella` chlorella tablets from foodin.
* `spirulina` spirulina tablets from foodin.
* `chocolate100` 100% dark chocolate. Yes, I consider this a supplement.
* `c8` brain octane oil from Bulletproof.
* `vitaminc` calcium ascorbate.
* `glutamin` L-Glutamin.
* `vitamind` in liquid form with MCT oil from Thorne Research.
* `omega3` MorDHA from Minami.
* `greentea` Kukicha tea from "in the mood for tea".
* `phosphatidylserine (g)` iso-phos product from Thorne Research. Value is in grams. No value means 0.
* `mela. (+Mg. PassFlor)` melatonin supplement including some extracts from chamomile and passion flower. Value is in mg. No value means 0.
* `mag` magnesium citramate from Thorne Research. 
* `magBisglyc` magnesium bisglycinate from Thorne Research. Value is in grams. No value means 0.
## Habits `hbts.csv`
This includes tracking of certain habits. Such as time restricted eating, sunlight exposure, sitting etc.

* `DAY` the day that these measurements are referring to in the format: `MM/DD/YYYY`.
* `TRE (12)` this means that my first meal of the day is at least 12 hours far from my last meal from the day before.
* `TRE (14)` this means that my first meal of the day is at least 14 hours far from my last meal from the day before.
* `WATER10h` this means that my first water drink of the day is at least 14 hours far from my last water drink from the day before.
* `Sunlight 5min` this means that I got exposed to sunlight for at least 5minutes a day.
* `IR` this is the time in minutes for how long I used an infrared lamp (from Joovv).
* `Fast` whether I fasted from both water and food until sunset that same day.
* `sitting` a subjective score for how good I did at moving during the day (and avoided sitting for too long). From 1 (sat down for too long, little movement) to 10 (did not sit down, moved very often). This measurement skips the value 7.
* `snacking` a subjective score for how good I avoided having many snacks during the day. From 1 (snacked often) to 10 (did not have any snacks). This measurement skips the value 7.
* `anxiety levels` a subjective score for how high my levels of anxiety were on that day. From 1 (no anxiety) to 10 (very anxious). This measurement skips the value 7.