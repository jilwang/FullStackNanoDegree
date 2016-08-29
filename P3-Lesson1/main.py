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

form = """
<form method="post">
    What is your birthday?
    <br>

    <label> Year
        <input type="text" name="Year">
    </label>

    <label> Month
        <input type="text" name="Month">
    </label>

    <label> Date
        <input type="text" name="Date">
    </label>

    <br>
    <br>
    <input type="submit">
</form>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    def post(self):
        import DateHelper
        user_year = DateHelper.valid_year(self.request.get('Year'))
        user_month = DateHelper.valid_month(self.request.get('Month'))
        user_date = DateHelper.valid_date(self.request.get('Date'))

        if not (user_year and user_month and user_date):
            if not user_year:
                print "Bad year ", user_year
            if not user_month:
                print "Bad month ", user_month
            if not user_date:
                print "Bad date: ", user_date
            self.response.out.write(form)
        else:
            self.response.out.write("Thanks! It's a valid date.")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
