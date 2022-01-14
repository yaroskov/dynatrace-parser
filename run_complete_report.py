from classes.dynatrace_parser.DynatraceParserRun import Run
from config import config

program = Run(config)
program.run_complete_report()
