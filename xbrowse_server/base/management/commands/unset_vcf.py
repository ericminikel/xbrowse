from optparse import make_option
import os

from django.core.management.base import BaseCommand

from xbrowse_server.base.models import Project, VCFFile


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--vcf-file', help='VCF File'),
        make_option('--all', action='store_true', dest='clear_all', default=False),
        )

    def handle(self, *args, **options):

        project_id = args[0]
        project = Project.objects.get(project_id=project_id)

        if options.get('clear_all'): 
            for individual in project.individual_set.all():
                individual.vcf_files.clear()
        else:
            vcf_file_path = os.path.abspath(options.get('vcf_file'))
            vcf_file = VCFFile.objects.get(file_path=vcf_file_path)
            for individual in project.individual_set.all():
                individual.vcf_files.remove(vcf_file)