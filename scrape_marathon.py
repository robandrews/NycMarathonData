from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import pdb
from time import sleep
import csv
import datetime

# Split this up however you wish, to break up the data
arr = [
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[2]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[3]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[4]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[5]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[6]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[7]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[8]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[9]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[10]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[11]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[12]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[13]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[14]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[15]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[16]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[17]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[18]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[19]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[20]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[21]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[22]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[23]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[24]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[25]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[26]",
      "/html/body/div[2]/form/table/tbody/tr[16]/td[2]/select/option[27]"
      ]


class MarathonScraper():

  def setUp(self):
    self.driver = webdriver.Firefox()
    self.csv_file = open("women18-90_" + str(datetime.date.today()) + ".csv", 'w')
    self.writer = csv.writer(self.csv_file)

  def scrape_age_group(self):
    driver = self.driver
    writer = self.writer
    rows = driver.find_elements_by_tag_name("tr")
    # Parent:
    # /html/body/div[2]/p[5]/table[1]/tbody/tr[2]
    # Child:
    # /html/body/div[2]/p[5]/table[1]/tbody/tr[2]/td[1]
        
    for idx, row in enumerate(rows):
      children = row.find_elements_by_xpath("./td")
      children_text = map(lambda x: x.text.encode('utf-8', 'ignore').strip(), children)
      if children_text[0] == "First Name":
        continue
      print("Runner: ", idx, " of ", len(rows), ".")
      writer.writerow(children_text)

    try:
      buttons = driver.find_elements_by_tag_name("input")
      button = next(b for b in buttons if "Next 100" in b.get_attribute("value"))
      button.click()
      self.scrape_age_group()
    except Exception, ex:
      print("No button found")

    
        



  def search_page_of_results(self, url):
    driver = self.driver
    writer = self.writer

    driver.get(url)

    for elem in arr:
      radio = driver.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[16]/td[1]/input")
      radio.click()
      dom_el = driver.find_element_by_xpath(elem)
      dom_el.click()
      button = driver.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[32]/td[2]/input")
      button.click()
      self.scrape_age_group()
      driver.get(url)

  def tearDown(self):
    self.driver.close()
    self.csv_file.close()

if __name__ == "__main__":
  url = "http://web2.nyrrc.org/cgi-bin/start.cgi/mar-programs/archive/archive_search.html"

  m = MarathonScraper()
  MarathonScraper.setUp(m)
  MarathonScraper.search_page_of_results(m, url)
  MarathonScraper.tearDown(m)
