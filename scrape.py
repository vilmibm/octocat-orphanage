import os

DIR = os.getcwd()

index_contents = None
with open(os.path.join(DIR, 'index.md.blank')) as f:
    index_contents = f.read()

IMG_DIR = os.path.join(DIR, 'cats')

TMPL = '''
<p>
    <a href="mailto:vilmibm@pm.me?subject=Claiming an Octocat">
      <img alt="octocat" src="cats/{filename}">
    </a>
</p>
'''

with open(os.path.join(DIR, 'index.md'), 'w') as f:
    f.write(index_contents)
    f.write('<div class="cats">')

    for img in os.listdir(IMG_DIR):
        f.write(TMPL.format(filename=img))

    f.write('</div>')
