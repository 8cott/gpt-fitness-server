--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.4 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: saved_plans; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.saved_plans (
    id integer NOT NULL,
    created_at timestamp without time zone,
    diet_plan text,
    workout_routine text,
    workout_summary text,
    diet_summary text,
    user_id integer,
    plan_name character varying(255)
);


ALTER TABLE public.saved_plans OWNER TO postgres;

--
-- Name: saved_plans_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.saved_plans_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.saved_plans_id_seq OWNER TO postgres;

--
-- Name: saved_plans_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.saved_plans_id_seq OWNED BY public.saved_plans.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    age integer,
    weight double precision,
    feet integer,
    inches integer,
    goals character varying(255),
    days_per_week integer,
    dietary_restrictions character varying(255),
    created_at timestamp without time zone,
    password_hash character varying(128),
    sex character varying(255)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: saved_plans id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.saved_plans ALTER COLUMN id SET DEFAULT nextval('public.saved_plans_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: saved_plans; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.saved_plans (id, created_at, diet_plan, workout_routine, workout_summary, diet_summary, user_id, plan_name) FROM stdin;
21	2023-09-21 13:47:07.845267	Day 1:\nBreakfast: Oatmeal with berries and a side of Greek yogurt\nLunch: Grilled chicken breast with mixed greens, cucumbers, and cherry tomatoes\nDinner: Baked salmon with roasted vegetables (broccoli, carrots, and bell peppers)\nSnack: Apple slices with almond butter\n\nDay 2:\nBreakfast: Whole wheat toast with avocado and poached eggs\nLunch: Quinoa salad with chickpeas, feta cheese, and spinach\nDinner: Grilled lean steak with steamed asparagus and sweet potato fries\nSnack: Greek yogurt with mixed nuts and honey\n\nDay 3:\nBreakfast: Protein smoothie (banana, spinach, almond milk, and protein powder)\nLunch: Grilled shrimp with quinoa and roasted zucchini\nDinner: Baked chicken breast with sautéed kale and brown rice\nSnack: Cottage cheese with sliced peaches and a drizzle of honey	Day 1: Bleepy Cardiovascular exercise (running or cycling) - 30 minutes\nStrength training (full-body workout) - 45 minutes\nAbdominal exercises (plank, crunches) - 15 minutes\n\nDay 2: Cardiovascular exercise (elliptical or swimming) - 30 minutes\nStrength training (upper body workout) - 45 minutes\nYoga or stretching - 15 minutes\n\nDay 3: Cardiovascular exercise (jumping rope or rowing) - 30 minutes\nStrength training (lower body workout) - 45 minutes\nHIIT workout (burpees, mountain climbers) - 15 minutes\n\nDay 4: Cardiovascular exercise (running or cycling) - 30 minutes\nStrength training (full-body workout) - 45 minutes\nAbdominal exercises (Russian twists, leg raises) - 15 minutes\n\nDay 5: Cardiovascular exercise (elliptical or swimming) - 30 minutes\nStrength training (upper body workout) - 45 minutes\nYoga or stretching - 15 minutes	This 1 workout routine was chosen as it incorporates both cardiovascular exercise and strength training for optimal weight loss results. The combination of different types of exercises helps to maintain a high calorie burn, build lean muscle, and improve overall fitness. The inclusion of abdominal exercises and stretching/yoga also helps in toning the core muscles and improving flexibility.	This diet plan focuses on providing balanced meals with a good mix of protein, carbohydrates, and healthy fats. It includes whole grains, lean protein sources, plenty of vegetables, and fruits. These foods provide essential nutrients, fiber, and antioxidants, supporting weight loss, maintaining muscle mass, and promoting overall health. The plan also incorporates snacks to prevent overeating and to keep energy levels stable throughout the day.	2	Bloopy Floop
22	2023-09-21 13:47:46.51139	Day 1:\nBreakfast: Oatmeal with berries and a side of Greek yogurt\nLunch: Grilled chicken breast with mixed greens, cucumbers, and cherry tomatoes\nDinner: Baked salmon with roasted vegetables (broccoli, carrots, and bell peppers)\nSnack: Apple slices with almond butter\n\nDay 2:\nBreakfast: Whole wheat toast with avocado and poached eggs\nLunch: Quinoa salad with chickpeas, feta cheese, and spinach\nDinner: Grilled lean steak with steamed asparagus and sweet potato fries\nSnack: Greek yogurt with mixed nuts and honey\n\nDay 3:\nBreakfast: Protein smoothie (banana, spinach, almond milk, and protein powder)\nLunch: Grilled shrimp with quinoa and roasted zucchini\nDinner: Baked chicken breast with sautéed kale and brown rice\nSnack: Cottage cheese with sliced peaches and a drizzle of honey	Day 1: Floofy Cardiovascular exercise (running or cycling) - 30 minutes\nStrength training (full-body workout) - 45 minutes\nFloofy training (full-body workout) - 45 minutes\nAbdominal exercises (plank, crunches) - 15 minutes\n\nDay 2: Cardiovascular exercise (elliptical or swimming) - 30 minutes\nStrength training (upper body workout) - 45 minutes\nYoga or stretching - 15 minutes\n\nDay 3: Cardiovascular exercise (jumping rope or rowing) - 30 minutes\nStrength training (lower body workout) - 45 minutes\nHIIT workout (burpees, mountain climbers) - 15 minutes\n\nDay 4: Cardiovascular exercise (running or cycling) - 30 minutes\nStrength training (full-body workout) - 45 minutes\nAbdominal exercises (Russian twists, leg raises) - 15 minutes\n\nDay 5: Cardiovascular exercise (elliptical or swimming) - 30 minutes\nStrength training (upper body workout) - 45 minutes\nYoga or stretching - 15 minutes	Fleefy floofy routine was chosen as it incorporates both cardiovascular exercise and strength training for optimal weight loss results. The combination of different types of exercises helps to maintain a high calorie burn, build lean muscle, and improve overall fitness. The inclusion of abdominal exercises and stretching/yoga also helps in toning the core muscles and improving flexibility.	This diet plan focuses on providing balanced meals with a good mix of protein, carbohydrates, and healthy fats. It includes whole grains, lean protein sources, plenty of vegetables, and fruits. These foods provide essential nutrients, fiber, and antioxidants, supporting weight loss, maintaining muscle mass, and promoting overall health. The plan also incorporates snacks to prevent overeating and to keep energy levels stable throughout the day.	2	Fleepy Floppy
23	2023-09-22 14:22:07.161709	Day 1:\n- Breakfast: Veggie omelet with egg whites, bell peppers, spinach, and onions.\n- Lunch: Grilled chicken breast with a side of roasted vegetables (e.g., broccoli, cauliflower, and carrots).\n- Dinner: Baked salmon with quinoa and steamed asparagus.\n- Snack: Greek yogurt with mixed berries.\n\nDay 2:\n- Breakfast: Overnight oats made with rolled oats, almond milk, chia seeds, and topped with sliced almonds.\n- Lunch: Turkey and avocado wrap with whole wheat tortilla, lettuce, and tomato.\n- Dinner: Grilled shrimp skewers with brown rice and grilled zucchini.\n- Snack: Apple slices with almond butter.\n\nDay 3:\n- Breakfast: Protein smoothie made with almond milk, banana, spinach, and protein powder.\n- Lunch: Quinoa salad with mixed greens, tomatoes, cucumbers, feta cheese, and grilled chicken.\n- Dinner: Baked chicken breast with sweet potato wedges and steamed green beans.\n- Snack: Carrot sticks with hummus.	Day 1:\n- Warm up: 5 minutes of light cardio (e.g., jogging or jumping jacks)\n- Strength training: 3 sets of squats, 3 sets of push-ups, 3 sets of dumbbell lunges, and 3 sets of seated rows.\n- Cardio: 20 minutes of steady-state cardio on the treadmill or stationary bike.\n- Cool down: 5 minutes of stretching exercises targeting major muscle groups.\n\nDay 2:\n- Warm up: 5 minutes of light cardio followed by dynamic stretching exercises.\n- HIIT workout: Alternating between 30 seconds of high-intensity exercises (e.g., burpees, mountain climbers, or squat jumps) and 30 seconds of active recovery exercises (e.g., walking or jogging in place). Repeat for 20-30 minutes.\n- Core workout: 3 sets of planks, 3 sets of Russian twists, and 3 sets of bicycle crunches.\n- Cool down: 5 minutes of static stretching.\n\nDay 3:\n- Warm up: 5 minutes of light cardio followed by dynamic stretching exercises.\n- Strength training: 3 sets of dumbbell bench press, 3 sets of bent-over rows, 3 sets of shoulder presses, and 3 sets of deadlifts.\n- Cardio: 25 minutes of interval training on the elliptical machine (alternating between high and low intensity every 2 minutes).\n- Cool down: 5 minutes of stretching exercises targeting major muscle groups.\n\nDay 4:\n- Warm up: 5 minutes of light cardio followed by dynamic stretching exercises.\n- Circuit training: Perform a circuit of 5-6 exercises (e.g., jumping squats, push-ups, kettlebell swings, mountain climbers, lunges, and tricep dips) with minimal rest between exercises. Complete 3-4 circuits.\n- Core workout: 3 sets of planks, 3 sets of leg raises, and 3 sets of reverse crunches.\n- Cool down: 5 minutes of static stretching.\n\nDay 5:\n- Warm up: 5 minutes of light cardio followed by dynamic stretching exercises.\n- Full-body workout: Perform compound exercises such as squats, deadlifts, bench press, shoulder press, and pull-ups. Complete 3 sets of each exercise with appropriate weights for your fitness level.\n- Cardio: 20 minutes of moderate-intensity cardio of your choice (e.g., cycling, swimming, or jogging).\n- Cool down: 5 minutes of stretching exercises targeting major muscle groups.	This workout routine includes a mix of strength training and cardio exercises to target different muscle groups and increase overall calorie burn. The combination of strength training and high-intensity interval training (HIIT) helps increase metabolism and burn fat efficiently. The circuit training and full-body workout sessions engage multiple muscle groups simultaneously for maximum calorie expenditure. The variety of exercises and progressive overload will challenge the body and help achieve weight loss goals.	The chosen diet plan focuses on incorporating lean protein sources, high-fiber carbohydrates, and various vegetables to support weight loss and provide essential nutrients. Each meal includes a balance of macronutrients while avoiding processed foods and excessive added sugars. The meals are designed to provide sustained energy throughout the day and promote satiety. Regular consumption of small, healthy snacks helps maintain stable blood sugar levels and prevent overeating. It is important to stay hydrated throughout the day and listen to the body's hunger and fullness cues while following this diet plan.	2	Planny Plan
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, email, age, weight, feet, inches, goals, days_per_week, dietary_restrictions, created_at, password_hash, sex) FROM stdin;
7	BLoofyFLoofy	floasjdfk@hotmail.com	\N	\N	\N	\N	\N	\N	\N	2023-09-18 17:13:06.45533	$2b$12$S1VGKyA2ftXJcW7TpXts1e./CCN2H9f4oHLi.GOmFNULCPMAZu41W	\N
8	Schmoofly	Schmoofly@gmail.com	\N	\N	\N	\N	\N	\N	\N	2023-09-18 17:20:00.028368	$2b$12$DDBBSuXCHl.CLMk1k973XutfuNEYKlO0Qh6ZGFLt8wDXz0itANZ1K	\N
9	TestUser1	testuser1@gmail.com	\N	\N	\N	\N	\N	\N	\N	2023-09-18 17:25:02.746665	$2b$12$jV8AAgap.wd93FJc4d/nKeRmrV2gWpUorvT6cGmG8WGTfIKz15EJ2	\N
10	werasdfsssss	asdfsadffs@hotmail.com	\N	\N	\N	\N	\N	\N	\N	2023-09-18 17:46:30.402075	$2b$12$vLYhXJpRP4oenJ9cea.iW.uuY/TzDkIO0jc4wrpnPoVZPjpPX0S3G	\N
11	testmetestme	testmeplease@gmail.com	\N	\N	\N	\N	\N	\N	\N	2023-09-20 09:20:41.195408	$2b$12$b7Uyx4Gj.7.L/q.mMXBYQuAthka0j4JmHwviSgQoSIgUV2SA8n842	\N
3	Biffy Schmiff	biffyshmiffy@gmail.com	33	200	5	9	lose weight	3	None	2023-09-01 15:32:45.779545	$2b$12$2u.oH6FSuU9qp.riiXT8h.CZnv2zjLLvq2XteEZ2Xw9UWUrxanECe	M
4	Kokface	kokface@gmail.com	23	300	4	4	lose weight	1	None	2023-09-06 15:30:03.366524	$2b$12$V6KhJSE.AoTRGbFJU6zP7.hzXV0F.VbBzCnxv8q01RCNAK9.SC3f.	M
6	Fluffykins	Fluffykins72@gmail.com	22	125	5	4	I want to lose 5 pounds in 12 weeks.	3	Caveman	2023-09-18 16:45:19.487425	$2b$12$KEqoqtItkjtfTVTWgI0ApuXwrRoGc.eIvjvH2Dgjzc112sT3k2AeK	F
2	8cott	scottrubin@gmail.com	47	176	5	10	Lose 5 lbs in 30 days.	5	None	2023-09-01 15:31:10.892877	$2b$12$4T9lkRJ/zCScAj4V6ufvr.ovcwHyj27S2tFKimhVVkgFtjeVO8n3e	M
12	thisisthelongestfuckingusernameever	fuckykins123@hotmal.org	\N	\N	\N	\N	\N	\N	\N	2023-09-21 10:40:37.283172	$2b$12$hMSkZnKpmPSGkZEHjFkU1.bT4/J.XbgVhszwOEZudvvEdMEvsIFme	\N
13	asdfawsefasdf	asdfas@asdfa.com	\N	\N	\N	\N	\N	\N	\N	2023-09-21 10:44:18.087014	$2b$12$93i2gsiV.KqgOlB.0s.qd.ikERkb6MyA29uUqV2PlOCEj1.J0DFQe	\N
14	dfghrfthhh	ghad@dxfgsfgh.com	\N	\N	\N	\N	\N	\N	\N	2023-09-21 10:51:52.038914	$2b$12$ogj2LWCjseCaNmMmJO7Qr.Bo5ClV2XyxMkRJuCs.D8KpcGW0MKJMK	\N
15	hfdgdfdfh	hjxdfgsdfg@gsdfg.com	\N	\N	\N	\N	\N	\N	\N	2023-09-21 10:55:31.437714	$2b$12$/7oJ.7Npa4MG5eC9nGjKNukOX/ETPdZ9tUdkT7wEF6S.o68lRd6xm	\N
16	dfghrfthhh3fsdf	jsh@jsnjjj.com	\N	\N	\N	\N	\N	\N	\N	2023-09-21 11:02:50.729975	$2b$12$Qdiepw/WCmUTbz8OJ8lb9OeJLHjRlHTdVf2TqhZ8s2CdmbOzbdQve	\N
17	kldfgj9kj	lhuyw@outlook.com	\N	\N	\N	\N	\N	\N	\N	2023-09-21 11:22:46.431455	$2b$12$VRJRu.Ff5YQr7f1Q1PYorOpFHbWanGzjR8PyLlW9CuX5OMWkwwPr.	\N
18	kldfgj9kj333	lhuyssw@outlook.com	\N	\N	\N	\N	\N	\N	\N	2023-09-21 11:23:03.764009	$2b$12$KVL7qy5RHeaE0BkoGvox0ukGrIKhJF7KGYpc07iWlV9nxwi5CxPyi	\N
19	ilwkhhh2	shnmwoo@gmail.com	\N	\N	\N	\N	\N	\N	\N	2023-09-21 11:24:17.528047	$2b$12$iCKGcSm7XdnmOkRpTw9eYODANPFQof1cc/8zpJB.XRHeKtKLqYq9K	\N
20	lastimemotherfucker	merfer@hotmail.com	\N	\N	\N	\N	\N	\N	\N	2023-09-21 11:31:12.206501	$2b$12$ZV2aTRAaSBdfPVx66E0RCOfjDWVERZT7QU.dvwGbFaxWoNa/7QOli	\N
\.


--
-- Name: saved_plans_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.saved_plans_id_seq', 23, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 20, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: saved_plans saved_plans_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.saved_plans
    ADD CONSTRAINT saved_plans_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_username; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_users_username ON public.users USING btree (username);


--
-- Name: saved_plans saved_plans_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.saved_plans
    ADD CONSTRAINT saved_plans_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

