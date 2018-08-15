# gazou-collector

Key Class Components

 * HtmlRetreiver : convert site url to html file 
   -> DynamicHtmlRetreiver 
   -> FixedHtmlRetreiver

 * HtmlSlicer : break html file into series of links 
   -> TitleSlicer : 
   -> ChapterSlicer 
   -> PageSlicer

 * ImgDownloader : given a link to an img, save an image to the storage

 * ImgDataManager : keep track of what's downloaded along with timestamps, avoid duplicates & suggest next one to download

Usage Scenario 1: 
  fixed web-site with .jpg files embed in img tag 
  if chapter base url is available, FixedHtmlRetreiver -> PageSlicer ->   ImgDownloader uses ImgDataManager


