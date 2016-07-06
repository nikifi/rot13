#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

form = """
<html>
  <form method="post" action="/">
  <h2>
  Enter some text to apply the ROT13 algorithm!
  </h2>
  <textarea rows="6" cols = "50" name="text">
  %(text)s
  </textarea>
  <br/>
  <input type="submit">
  </form>
</html>

"""


class MainHandler(webapp2.RequestHandler):

    def write_form(self, text=""):
        self.response.out.write(form %{"text": self.escape_html(text)})

    def get(self):
        self.write_form()
        
        

    def post(self):
        name = self.request.get('text')
        if name:
            self.write_form(self.rot(name))


    def escape_html(self, s):
    
      newstring = s
      newstring = newstring.replace('&', '&amp;')
      newstring = newstring.replace('>', '&gt;')
      newstring = newstring.replace('<', '&lt;')
      newstring = newstring.replace('"', '&quot;')
      return newstring

    def rot(self, text):
        final_string = ""
        build_string = ""

        dict = {'A' : 'N',
                'B': 'O',
                'C' : 'P',
                'D' : 'Q',
                'E' : 'R',
                'F' : 'S',
                'G' : 'T',
                'H' : 'U',
                'I' : 'V',
                'J' : 'W',
                'K' : 'X',
                'L' : 'Y',
                'M' : 'Z',
                'N' : 'A',
                'O' : 'B',
                'P' : 'C',
                'Q' : 'D',
                'R' : 'E',
                'S' : 'F',
                'T' : 'G',
                'U' : 'H',
                'V' : 'I',
                'W' : 'J',
                'X' : 'K',
                'Y' : 'L',
                'Z' : 'M'}  
        
        for characters in text:
          if dict.get(characters.upper()):
            if characters.isupper():
                build_string = build_string + dict.get(characters.upper()).upper()
            else: 
                build_string = build_string + dict.get(characters.upper()).lower()
          else:
            build_string = build_string + characters
        return build_string
         



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
