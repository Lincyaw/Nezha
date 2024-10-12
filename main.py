from pattern_ranker import *
import argparse


log_path = "." + '/log/' + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '_nezha.log'
print(log_path)
logger = Logger(log_path, logging.DEBUG, __name__).getlog()


def get_miner(ns):
    template_indir = '.' + '/log_template'
    config = TemplateMinerConfig()
    config.load('.' + "/log_template/drain3_" + ns + ".ini")
    config.profiling_enabled = False

    path = '.' + '/log_template/' + ns + ".bin"
    persistence = FilePersistence(path)
    template_miner = TemplateMiner(persistence, config=config)

    return template_miner

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Nezha')

    parser.add_argument('--ns', default="hipster", help='namespace')
    parser.add_argument('--level', default="service", help='service-level or inner-service level')

    args = parser.parse_args()
    ns = args.ns
    level = args.level

    if ns == "hipster":
        normal_time1 = "2022-08-22 03:51"
        path1 = '.' +  "/rca_data/2022-08-22/2022-08-22-fault_list.json"

        log_template_miner = get_miner(ns)
        inject_list = [path1]
        normal_time_list = [normal_time1]
        if level=="service":
            logger.info("------- OnlineBoutique Result at service level -------")
            evaluation_pod(normal_time_list, inject_list, ns,log_template_miner)
        else:
            logger.info("------- OnlineBoutique Result at inner service level -------")
            evaluation(normal_time_list, inject_list, ns,log_template_miner)
