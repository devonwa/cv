---
layout: default
title: CV
---

{::options parse_block_html="true" /}
<div class="cv">
{% raw %}
<div class="text-center">
# Devon Walker
[PDF](/static/page/cv/Devon-Walker-Resume.pdf)
&#124;
[source](https://github.com/devonwa/cv)
&#124;
<a href="mailto:{% include email.html %}">{% include email.html %}</a>
<br />
<br />
**I am currently seeking internship opportunities between January and August 2017, before entering a Ph.D. program in the fall.**
</div>
{% endraw %}

## Education
<hr>

{% for item in education %}
**{{ item.school }}** <span class="pull-right">{{ item.date }}</span><br />
{{ item.degree }} (GPA: {{ item.gpa }})<br />

{% if item.details %}
{% for detail in item.details %}
* {{ detail }}
{% endfor %}
{% endif %}
<br />
{% endfor %}

## Research
<hr>

{% for item in research %}
**{{ item.name }}** <span class="pull-right">{{ item.location }}</span><br />
{{ item.title }} <span class="pull-right">{{ item.dates }}</span><br />
{% for p in item.project %}
{{ p.title }}

{% if p.details %}
{% for detail in p.details %}
* {{ detail }}
{% endfor %}
{% else %}
{% endif %}
{% endfor %}
<br />
{% endfor %}

## Industry
<hr>

{% for item in industry %}
**{{ item.company }}** <span class="pull-right">{{ item.location }}</span><br />
{{ item.title }} <span class="pull-right">{{ item.dates }}</span><br />

{% if item.details %}
{% for detail in item.details %}
{% if detail is string %}
* {{ detail }}
{% else %}
{% for subdetail in detail %}
  * {{ subdetail }}
{% endfor %}
{% endif %}

{% endfor %}
{% endif %}
{% if not loop.last %}
<br />
{% endif %}
{% endfor %}

## Certificates
<hr>

{% for item in certificates %}
**{{ item.name }}** <span class="pull-right">{{ item.date }}</span>
{% endfor %}

## Skills
<hr>

{% for item in skills %}
**{{ item.type }}:** {{ item.details }}
<br />
{% if not loop.last %}
<br />
{% endif %}
{% endfor %}

## Affiliations
<hr>

{% for item in affiliations %}
**{{ item.organization }}** <span class="pull-right">{{ item.title }}, {{ item.dates }}</span>
<br />
{% endfor %}
</div>
