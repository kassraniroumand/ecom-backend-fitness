from app.schemas import Category, CategoryProduct


def _p(
    pid: str,
    name: str,
    price: str,
    finance: str,
    features: list[str],
    img: str,
    *,
    badge: str | None = None,
    price_label: str = "از",
    dark: bool = False,
) -> CategoryProduct:
    return CategoryProduct(
        id=pid,
        name=name,
        badge=badge,
        priceLabel=price_label,
        price=price,
        finance=finance,
        features=features,
        img=img,
        dark=dark,
    )


running = Category(
    slug="running",
    crumb="تردمیل‌ها",
    eyebrow="هوازی — ۴ زیرشاخه",
    title="تردمیل‌های طراحی‌شده برای دویدن واقعی",
    description=(
        "کاهش وزن، حفظ تناسب اندام و ارتقای عملکرد با تردمیل‌های جایزه‌برده‌ی ما "
        "برای تجربه‌ی تمرین خانگی همه‌جانبه و ایمن. مهندسی‌شده در ایتالیا. مورد اعتماد "
        "ورزشکاران، طراحان و المپیکی‌ها برای بیش از ۴۰ سال."
    ),
    filters=["همه", "خانگی", "استودیو", "حرفه‌ای", "جمع‌وجور", "هوشمند"],
    products=[
        _p("run", "تکنوجیم ران", "۱۰,۷۲۰ پوند", "پرداخت اقساطی ۳۶ ماهه با بهره‌ی ۰٪", ["حالت سورتمه‌ای", "نرم و کم‌صدا", "تمرین‌های گروهی"], "/assets/latest-run.png"),
        _p("myrun", "تکنوجیم مای‌ران", "۳,۶۵۰ پوند", "پرداخت اقساطی ۳۶ ماهه با بهره‌ی ۰٪", ["ابعاد جمع‌وجور", "سطح دویدن وفق‌پذیر", "اتصال به تبلت شما"], "/assets/latest-run.png"),
        _p("run-personal", "ران پرسونال", "۱۳,۴۵۰ پوند", "پرداخت بعدی با کلارنا", ["طراحی منحصربه‌فرد", "دویدن راحت", "نمایشگر ۲۲ اینچی"], "/assets/latest-run.png", badge="طراحی آنتونیو سیتریو", price_label="", dark=True),
        _p("skillrun", "اسکیل‌ران", "۱۸,۹۰۰ پوند", "تأمین مالی ویژه‌ی کسب‌وکار در دسترس است", ["فناوری مالتی‌درایو", "حالت تمرین سورتمه‌ای", "داشبورد عملکرد"], "/assets/latest-run.png", badge="حرفه‌ای"),
    ],
    bottomEyebrow="ساخته‌شده برای ماندگاری — مهندسی در چزنا",
    bottomTitleLead="چهل سال تحقیق",
    bottomTitleAccent="دویدن",
    bottomTitleTail="، در هر تسمه.",
)


strength = Category(
    slug="strength",
    crumb="تجهیزات قدرتی",
    eyebrow="قدرتی — ۵ زیرشاخه",
    title="قدرت ناب، طراحی‌شده برای خانه و باشگاه",
    description=(
        "از دمبل‌های هوشمند تا مالتی‌جیم‌های جمع‌وجور، تجهیزات قدرتی ما برای فرم‌دهی، "
        "مجسمه‌سازی و افزایش قدرت در هر فضایی طراحی شده‌اند. کیفیت ساخت ایتالیایی، با "
        "ضمانت بلندمدت."
    ),
    filters=["همه", "وزنه آزاد", "مالتی‌جیم", "نیمکت", "هوشمند", "جمع‌وجور"],
    products=[
        _p("dumbbell-set", "ست دمبل هوشمند", "۵۹۹ پوند", "پرداخت اقساطی ۲۴ ماهه با بهره‌ی ۰٪", ["تنظیم وزن لمسی", "ردیابی تکرارها", "پایه‌ی شارژ"], "/assets/latest-dumbbells.png", badge="جدید"),
        _p("power-station", "پاور استیشن", "۴,۹۹۰ پوند", "پرداخت اقساطی ۳۶ ماهه با بهره‌ی ۴.۹٪", ["مقاومت وفق‌پذیر", "برج جمع‌وجور", "اتصال به اپلیکیشن"], "/assets/latest-multigym.png", dark=True),
        _p("multi-bench", "نیمکت چندکاره", "۸۹۰ پوند", "پرداخت اقساطی ۲۴ ماهه با بهره‌ی ۰٪", ["زاویه‌ی قابل تنظیم", "تاشو", "روکش چرم مصنوعی"], "/assets/latest-dumbbells.png"),
        _p("kinesis-personal", "کینسیس پرسونال", "۱۵,۴۰۰ پوند", "تأمین مالی شخصی موجود است", ["مقاومت سه‌بعدی", "بدون نیاز به وزنه", "طراحی نمایشی"], "/assets/latest-multigym.png", badge="طراحی آنتونیو سیتریو", price_label="", dark=True),
    ],
    bottomEyebrow="مهندسی قدرت — ساخت ایتالیا",
    bottomTitleLead="هر تکرار،",
    bottomTitleAccent="قدرتمندتر",
    bottomTitleTail=" از قبل.",
)


bike = Category(
    slug="bike",
    crumb="دوچرخه‌ها",
    eyebrow="استقامت — ۳ زیرشاخه",
    title="دوچرخه‌های ثابتی که با شما همراه‌اند",
    description=(
        "از کلاس‌های زنده تا تور آزاد در جاده‌های مجازی، دوچرخه‌های ما تجربه‌ی "
        "رکاب‌زنی استودیویی را به خانه‌ی شما می‌آورند. مقاومت مغناطیسی بی‌صدا و "
        "نمایشگر متصل."
    ),
    filters=["همه", "استودیو", "ریکامبنت", "ایندور", "حرفه‌ای", "جمع‌وجور"],
    products=[
        _p("bike-studio", "بایک استودیو", "۲,۴۹۰ پوند", "پرداخت اقساطی ۳۶ ماهه با بهره‌ی ۴.۹٪", ["مقاومت مغناطیسی", "کلاس‌های زنده", "نمایشگر قابل تنظیم"], "/assets/latest-bike.png", badge="جدید"),
        _p("bike-personal", "بایک پرسونال", "۹,۲۰۰ پوند", "پرداخت بعدی با کلارنا", ["قاب چرمی", "حالت بی‌صدا", "تجربه‌ی نمایشی"], "/assets/latest-bike.png", badge="طراحی آنتونیو سیتریو", price_label="", dark=True),
        _p("skillbike", "اسکیل‌بایک", "۶,۸۰۰ پوند", "تأمین مالی ویژه‌ی کسب‌وکار در دسترس است", ["شبیه‌سازی دنده", "حالت رقابتی", "پایش توان"], "/assets/latest-bike.png", badge="حرفه‌ای"),
        _p("myride", "مای‌راید", "۱,۲۹۰ پوند", "پرداخت اقساطی ۲۴ ماهه با بهره‌ی ۰٪", ["تاشو", "اتصال به تبلت", "وزن سبک"], "/assets/latest-bike.png"),
    ],
    bottomEyebrow="ساخته‌شده برای رکاب — مهندسی در چزنا",
    bottomTitleLead="هر چرخش،",
    bottomTitleAccent="روان‌تر",
    bottomTitleTail=" از قبل.",
)


wellness = Category(
    slug="wellness",
    crumb="تندرستی",
    eyebrow="تندرستی — ۴ زیرشاخه",
    title="تمرین ذهن و بدن، در خانه‌ی شما",
    description=(
        "ابزارهای ریکاوری، پوشیدنی‌های هوشمند و تمرین‌های ذهن‌آگاهانه برای زندگی "
        "متعادل. هر روز بهتر از دیروز."
    ),
    filters=["همه", "ریکاوری", "پوشیدنی", "ذهن‌آگاهی", "هوشمند", "سفر"],
    products=[
        _p("myrun-tracker", "ردیاب مای‌ران", "۳۴۹ پوند", "پرداخت اقساطی ۴ ماهه با بهره‌ی ۰٪", ["ردیابی ضربان", "اتصال به اپلیکیشن", "ضدآب"], "/assets/latest-watch.png", badge="جدید"),
        _p("recovery-kit", "کیت ریکاوری", "۱۴۹ پوند", "پرداخت اقساطی ۴ ماهه با بهره‌ی ۰٪", ["ماساژر برقی", "نوار کشی", "غلتک فوم"], "/assets/latest-recovery.png", badge="جدید"),
        _p("mindful-mat", "تشک ذهن‌آگاه", "۸۹ پوند", "پرداخت یک‌جا یا با کلارنا", ["جنس طبیعی", "تاشو", "همراه با کیف"], "/assets/latest-recovery.png"),
        _p("wellness-ring", "حلقه‌ی تندرستی", "۲۹۹ پوند", "پرداخت اقساطی ۶ ماهه با بهره‌ی ۰٪", ["پایش خواب", "ردیابی استرس", "باتری ۷ روزه"], "/assets/latest-watch.png", badge="نسل دوم", dark=True),
    ],
    bottomEyebrow="تندرستی — ساخته‌شده برای زندگی روزمره",
    bottomTitleLead="تعادل،",
    bottomTitleAccent="هر روز",
    bottomTitleTail=" از سال.",
)


CATEGORIES_BY_SLUG: dict[str, Category] = {
    "running": running,
    "strength": strength,
    "bike": bike,
    "wellness": wellness,
}

HERO_IMAGES: dict[str, str] = {
    "running": "/assets/cat-treadmills.jpg",
    "strength": "/assets/cat-freeweights.jpg",
    "bike": "/assets/cat-bikes.jpg",
    "wellness": "/assets/wellness.jpg",
}


def all_categories() -> list[Category]:
    return list(CATEGORIES_BY_SLUG.values())


def get_category(slug: str) -> Category | None:
    return CATEGORIES_BY_SLUG.get(slug)


def find_product(product_id: str) -> tuple[CategoryProduct, Category] | None:
    for category in CATEGORIES_BY_SLUG.values():
        for product in category.products:
            if product.id == product_id:
                return product, category
    return None


def related_products(
    category: Category,
    exclude_id: str,
    limit: int = 3,
) -> list[CategoryProduct]:
    return [p for p in category.products if p.id != exclude_id][:limit]
