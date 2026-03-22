curriculum_vitae_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ full_name }} | Curriculum Vitae</title>
    <style>
        :root {
            color-scheme: light;
            --text: #111827;
            --muted: #4b5563;
            --line: #e5e7eb;
            --soft: #f8fafc;
            --accent: #111827;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f4f6;
            color: var(--text);
            line-height: 1.6;
        }

        .page {
            max-width: 1080px;
            margin: 32px auto;
            background: #ffffff;
            border: 1px solid var(--line);
            box-shadow: 0 16px 40px rgba(15, 23, 42, 0.08);
        }

        .hero {
            padding: 40px 48px 28px;
            border-bottom: 1px solid var(--line);
        }

        .hero h1 {
            margin: 0;
            font-size: 2.2rem;
            letter-spacing: 0.06em;
        }

        .hero .role {
            margin-top: 8px;
            font-size: 1rem;
            color: var(--muted);
            font-weight: 600;
        }

        .contact {
            margin-top: 18px;
            display: flex;
            flex-wrap: wrap;
            gap: 10px 18px;
            font-size: 0.95rem;
            color: var(--muted);
        }

        .contact a {
            color: var(--accent);
            text-decoration: none;
        }

        .content {
            display: grid;
            grid-template-columns: 1.25fr 0.75fr;
        }

        .main,
        .side {
            padding: 32px 48px;
        }

        .side {
            background: var(--soft);
            border-left: 1px solid var(--line);
        }

        section + section {
            margin-top: 28px;
        }

        h2 {
            margin: 0 0 14px;
            font-size: 0.95rem;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--accent);
        }

        p {
            margin: 0;
        }

        .entry + .entry {
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid var(--line);
        }

        .entry-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 16px;
            margin-bottom: 8px;
        }

        .entry-title {
            font-size: 1.05rem;
            font-weight: 700;
        }

        .entry-subtitle {
            color: var(--muted);
            font-weight: 600;
        }

        .entry-period {
            white-space: nowrap;
            color: var(--muted);
            font-size: 0.92rem;
        }

        ul {
            margin: 10px 0 0;
            padding-left: 18px;
        }

        li + li {
            margin-top: 6px;
        }

        .stack-group + .stack-group,
        .simple-list + .simple-list {
            margin-top: 16px;
        }

        .stack-group h3,
        .simple-list h3 {
            margin: 0 0 6px;
            font-size: 0.95rem;
        }

        .chips {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .chip {
            border: 1px solid var(--line);
            background: #ffffff;
            border-radius: 999px;
            padding: 6px 10px;
            font-size: 0.88rem;
        }

        @media (max-width: 860px) {
            .content {
                grid-template-columns: 1fr;
            }

            .side {
                border-left: 0;
                border-top: 1px solid var(--line);
            }

            .hero,
            .main,
            .side {
                padding: 28px 24px;
            }

            .entry-header {
                flex-direction: column;
            }

            .entry-period {
                white-space: normal;
            }
        }
    </style>
</head>
<body>
    <div class="page">
        <header class="hero">
            <h1>{{ full_name }}</h1>
            <div class="role">{{ role }}</div>
            <div class="contact">
                <span>{{ location }}</span>
                <a href="tel:{{ phone }}">{{ phone }}</a>
                <a href="mailto:{{ email }}">{{ email }}</a>
                <a href="{{ github_url }}" target="_blank">GitHub: {{ github_handle }}</a>
            </div>
        </header>

        <div class="content">
            <main class="main">
                <section>
                    <h2>Professional Summary</h2>
                    <p>{{ professional_summary }}</p>
                </section>

                <section>
                    <h2>Professional Experience</h2>
                    {% for item in professional_experience %}
                    <div class="entry">
                        <div class="entry-header">
                            <div>
                                <div class="entry-title">{{ item.title }}</div>
                                <div class="entry-subtitle">{{ item.company }}</div>
                            </div>
                            <div class="entry-period">{{ item.period }}</div>
                        </div>
                        <ul>
                            {% for detail in item.details %}
                            <li>{{ detail }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                    {% endfor %}
                </section>

                <section>
                    <h2>Internships & Early Experience</h2>
                    <ul>
                        {% for item in internships_and_early_experience %}
                        <li>{{ item }}</li>
                        {% endfor %}
                    </ul>
                </section>

                <section>
                    <h2>Education</h2>
                    {% for item in education %}
                    <div class="entry">
                        <div class="entry-header">
                            <div class="entry-title">{{ item.institution }}</div>
                            <div class="entry-period">{{ item.period }}</div>
                        </div>
                        <p>{{ item.details }}</p>
                    </div>
                    {% endfor %}
                </section>
            </main>

            <aside class="side">
                <section>
                    <h2>Technical Stack</h2>
                    {% for category, items in technical_stack.items() %}
                    <div class="stack-group">
                        <h3>{{ category }}</h3>
                        <div class="chips">
                            {% for item in items %}
                            <span class="chip">{{ item }}</span>
                            {% endfor %}
                        </div>
                    </div>
                    {% endfor %}
                </section>

                <section>
                    <h2>Languages</h2>
                    <ul>
                        {% for item in languages %}
                        <li>{{ item }}</li>
                        {% endfor %}
                    </ul>
                </section>

                <section>
                    <h2>Additional Strengths</h2>
                    <ul>
                        {% for item in additional_strengths %}
                        <li>{{ item }}</li>
                        {% endfor %}
                    </ul>
                </section>
            </aside>
        </div>
    </div>
</body>
</html>
'''
