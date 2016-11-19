import requests
from lxml import html


class Search(object):
    _cache = dict()

    @staticmethod
    def search_companies_with_similar_jobs(records_dict, job_selected):
        """ searching dict {url, xpath} """

        companies_url = set()
        for url, xpath in records_dict.items():

            try:
                page = requests.get(url)
                # create xml tree for the source code
                tree = html.fromstring(page.content)
                # set pattern to get information
                jobs = tree.xpath(xpath)

                # compatibility criteria
                job_criteria_list = job_selected.split()

                for job in jobs:
                    for item in job_criteria_list:
                        if item in job:
                            companies_url.add(url)

            except requests.exceptions.ConnectionError:
                raise
            except requests.exceptions.MissingSchema:
                raise

        return companies_url

    def search_jobs(self, job_url, xpath):
        """
            Parsing remote job_url for xpath data

            Args:
                job_url: URL where to search
                xpath: pattern that is used in the search

            Returns: A list of jobs or list of error messages

        """
        if self._is_in_cache(job_url):
            return self._get_cache(job_url)

        try:

            page = requests.get(job_url)
            # create xml tree for the source code
            tree = html.fromstring(page.content)
            # set pattern to get information
            jobs = tree.xpath(xpath)

            self._update_cache(job_url, jobs)

        except requests.exceptions.ConnectionError:
            jobs = ("<!> Connection error...",)
        except requests.exceptions.MissingSchema:
            jobs = ("<!> Invalid URL selected...",)

        return jobs
        # print("\n".join(jobs))

    @staticmethod
    def _update_cache(job_url, jobs):
        Search._cache[job_url] = jobs

    @staticmethod
    def _is_in_cache(job_url_key):
        return job_url_key in Search._cache

    @staticmethod
    def _get_cache(job_url_key):
        if job_url_key in Search._cache:
            return Search._cache[job_url_key]
